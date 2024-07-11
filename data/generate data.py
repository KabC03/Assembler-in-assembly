#Generates the data section for the asm program

import sys;

dataFileName = "data.asm";


preAppendDefines = {

    #File processing
    "LINE_BUFFER_SIZE" : 1000, 

    #Hashmap
    "HASH_TABLE_SIZE" : 100,
    "KEY_LENGTH" : 3,
    "DJB2_HASH_SEED" : 5381,
};




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




#Write data section
def write_data_section() :
    try:
        with open(dataFileName, 'a') as file:

            file.write("; .data section\n");
            file.write("section .data\n");

        return True;
    except:
        return False;



def main():

    #MUST call this first - since it opens for writing NOT appending
    if(write_defines() == False):
        print("Failed to write defines section\n");
        return -1;



    if(write_data_section() == False):
        print("Failed to write data section\n");
        return -2;


    return 0;



if __name__ == "__main__":
    sys.exit(main());













