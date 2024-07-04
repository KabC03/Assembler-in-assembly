//Some basic pseudocode for the main loop


int main(void) {


    out = open(outputFile);
    input = open(inputFile);



    while(input -> currentLine != EOF) {
        

        while(currentToken != NULL) {

            currentToken = strtok(currentLine, " ");
            
            if(currentToken == NULL) {
                break;
            } else {

                machineCode = hashmap_get(currentToken);

                if(machineCode == NULL) {
                    printf("Unexpected token");
                    return -1;
                    
                } else {

                    fwrite(out, machineCode);
                }

            }

        }



    }


    return 0;
}






 
