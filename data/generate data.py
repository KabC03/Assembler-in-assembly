#Generates the data section for the asm program - also write the hash table in assembly

import sys;

dataFileName = "data.asm";
djb2Hash = 0; #Will get changed by perfect hash function generator

preAppendDefines = {

    #File processing
    "LINE_BUFFER_SIZE" : 1000, 

    #Hashmap
    "HASH_TABLE_SIZE" : 100,
    "KEY_LENGTH" : 3,
    "DJB2_HASH_SEED" : 5381,
};


#Number of bytes required for inidividual items
pneumonicLength = 3;
machineCodeLength = 1;
sourceCodePneumonocs = {

    #Pneumonic : Machine code

    #Instructions
    "ADD" : "0", "LIR" : "1", "PSH" : "2", "POP" : "3", "JEQ" : "4", "BLK" : "-1",

    #Registers
    "EAX" : "0", "EBX" : "1", "ECX" : "2", "EDX" : "3",

};



#Iterate through lots of starting seeds to see if a perfect table was generated
def find_perfect_hash_constant():

    #Blank array to store hashes
    hashTable = list(sourceCodePneumonocs.keys());
    hashTableIsPerfect = False;


    #Set this to the blank list value - its inefficient but garuntees a blank element is not mistaken for one in the list
    blankValue = "".join(hashTable)

    while(hashTableIsPerfect == False):
        
        #For each element, hash it, if it collides with another element then table is not perfect - iterate seed











def write_defines():
    try:
        with open(dataFileName, 'w') as file:

            file.write("; Defines section\n\n");

            for key, value in preAppendDefines.items():
                file.write("%define " + str(key) + " " + str(value) + "\n");


            file.write("\n\n\n");

        return True;
    except:
        return False;




#Write .data section
def write_data_section() :
    try:
        with open(dataFileName, 'a') as file:

            file.write("; .data section\n");
            file.write("section .data\n");


            file.write("\n\n\n");
        return True;
    except:
        return False;


#Write .bss section
def write_bss_section():


    try:
        with open(dataFileName, 'a') as file:

            file.write("; .bss section\n");
            file.write("section .bss\n");

            #Space for key hashmap
            #file.write("    keyBuffer: db " + str(len(sourceCodePneumonocs.keys()) * pneumonicLength) + "\n"); #Keys dont need to be stored
            file.write("    valueBuffer: db " + str(len(sourceCodePneumonocs.values()) * machineCodeLength) + "\n");




        return True;
    except:
        return False;


def main():

    if(find_perfect_hash_constant() == False):
        print("Failed to find perfect hash seed\n");
        return -1;

    #MUST call this first - since it opens for writing NOT appending
    if(write_defines() == False):
        print("Failed to write defines section\n");
        return -2;
    if(write_data_section() == False):
        print("Failed to write .data section\n");
        return -3;
    if(write_bss_section() == False):
        print("Failed to write .bss section");
        return -4;



    return 0;



if __name__ == "__main__":
    sys.exit(main());

























