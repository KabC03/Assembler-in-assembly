#Copied from https://github.com/KabC03/Library-collection-in-C
#12 Aug 2024
'''
Generates a Lagrange polynomial that interpolates an x and y vector

Polynomial is encoded into x86 assembly



This creates a direct mapping of the inputs to the output - f(key) = value, for all keys and value
'''
import sys;
import math;

#Vectors to fit
sourceCodePneumonics = {

    #NOTE: Could technically have multi-char pneumonics here - but makes it much harder to not go over 64 bit integer limit


    #Pneumonic : Machine code
    "A" : "0", "L" : "1", "J" : "2",

    #Registers
    "X" : "0", "Y" : "1",


    #"R0" : "0", "R1" : "1", "R2" : "2", "R3" : "3",

};
outputFilePath = "./data/polymap.asm";




#Check for overflows
MAX_BYTES = 4;
BITS_PER_BYTE = 8;
BYTES_PER_CHAR = 1;





#Preprocess pneumonics to put them into binary form
def preprocess_pneumonics(sourceCodePneumonicsInput):

    keys = [];
    values = [];

    for key, value in sourceCodePneumonicsInput.items():

        if(len(key) > MAX_BYTES * BYTES_PER_CHAR or len(value) > MAX_BYTES * BYTES_PER_CHAR): #String cannot be longer than 8 bytes (must fit in reg)
            print("ERROR: key: '" + str(key) + "' or value: '" + str(value) + "' overflows set byte limit, max char limit is: " + str(int(MAX_BYTES * BYTES_PER_CHAR)));
            return keys, values, 1;



        newKey = "";
        newValue = "";

        for char in key:
            newKey += str(ord(char));
        
        for char in value:
            newValue += str(ord(char));

        keys.append(int(newKey));
        values.append(int(newValue));

    return keys, values, 0;



#Generate the map and assembly
def generate_Lagrange_map(keys, values):

    print("Lagrange polynomial:");

    if(len(keys) != len(values)):
        print("ERROR: Keys and values vectors are not the same length || keys = " + str(len(keys)) + " values = " + str(len(values)));
        return 1;


    try:

        with open(outputFilePath, 'w') as file:


            #Setup
            file.write("; 12 Aug, 2024\n");
            file.write("section .text\n\n\n\n\n");


            file.write("; edx polymap_get_value(eax key)\n");
            file.write("polymap_get_value:\n\n");
            file.write("    mov ebp, esp\n\n");

            file.write("; Setup\n");
            file.write("    push ebp\n");
            file.write("    push eax\n");
            file.write("    push ebx\n");
            file.write("    push ecx\n\n\n\n\n");


            # eax - contains key
            # ebx - temp
            # ecx - temp
            # edx - value

            file.write("; Evaluate polynomial at eax\n");
            #NOTE: For now this just prints text to the console - make it output to a .asm file later

            useEDXinsteadOfECX = True; #ONLY the first time, replace EDX with ECX - slightly more efficient

            for i in range(0, len(keys)):


                leadingCoefficient = values[i];
                print(str(leadingCoefficient) + " * (", end = '');


                print("(", end = '');
                firstLoad = True;
                for j in range(0, len(keys)): #Numerator
                    
                    if keys[j] != keys[i]:
                        print("(x - " + str(keys[j]) + ") ", end = '');
                
                        # (x - 74)
                        if(firstLoad == True): #First column of row, use ecx, avoids multiplication by 1

                            if(useEDXinsteadOfECX == True):
                                file.write("\n    mov edx, eax\n");
                                file.write("    sub edx, " + str(keys[j]) + "\n\n");
                            
                            else:
                                file.write("\n    mov ecx, eax\n");
                                file.write("    sub ecx, " + str(keys[j]) + "\n\n");
                        
                            #NOTE: Dont do any multiplication here
                            firstLoad = False;
                
                        else:
                            file.write("    mov ebx, eax\n");
                            file.write("    sub ebx, " + str(keys[j]) + "\n");


                            #(x - 76) * (x - 74)
                            if(useEDXinsteadOfECX == True):
                                file.write("    mul edx, ebx\n");
                            
                            else:
                                file.write("    mul ecx, ebx\n");

                

                #Multiply by numerator
                if(useEDXinsteadOfECX == True):
                    file.write("    mul edx, " + str(leadingCoefficient) + "\n");
                
                else:
                    file.write("    mul ecx, " + str(leadingCoefficient) + "\n");





                print(" / ", end = '');
                denominator = 1;
                for j in range(0, len(keys)): #Denominator

                    if keys[j] != keys[i]:
                        #Denominator
                        denominator *= keys[i]- keys[j];


                #NOTE: Numerator and denominator are not simplified further to avoid float precision issues

                print(str(denominator) + ")", end = '');
                        


                #Divide by denominator
                if(useEDXinsteadOfECX == True):
                    file.write("    div edx, " + str(denominator) + "\n");
                
                else:
                    file.write("    div ecx, " + str(denominator) + "\n");




                print(") + ");
            

                signedIntegerLimit = int(pow(2, (BITS_PER_BYTE * MAX_BYTES))/2);
                if(denominator > signedIntegerLimit):
                    print("ERROR: denominator '" + str(denominator) + "' exceeds " + str(MAX_BYTES) + " byte signed limit (" + str(signedIntegerLimit) + ")");
                    print("Overflow factor: " + str(denominator/ (signedIntegerLimit)));
                    return 1;
        




                #Add row to accumulator
                if(i == 0): #EDX already contains the row
                    pass;
                else:
                    file.write("    add edx, ecx\n");








                useEDXinsteadOfECX = False;

            file.write("\n\n\n\n\n\n");

            #Cleanup
            file.write("; Cleanup\n");
            file.write("    mov esp, ebp\n");
            file.write("    pop ecx\n");
            file.write("    pop ebx\n");
            file.write("    pop eax\n");
            file.write("    pop ebp\n");
            file.write("    ret\n");

    except:
        print("File failed to open");
        return 1;

    return 0;








def main():

    keys = [];
    values = [];
    sourceCodePneumonicsInput = sourceCodePneumonics;

    keys, values, returnCode = preprocess_pneumonics(sourceCodePneumonicsInput);
    if(returnCode != 0):
        return 1;

    if(generate_Lagrange_map(keys, values) != 0):
        return 1;

    return 0;


if __name__ == "__main__":
    sys.exit(main());




