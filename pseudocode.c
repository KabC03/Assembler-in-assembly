




void dict_store(token, machineCode) {


    for(i < numTokens) {

        keys[i] = token;
        values[i] = machineCode;
    }


    return; 
}


value dict_get(token) {



    for(i < numTokens) {
        if(token == keys[i]) {
            return values[i];
        }
    }


    return NULL;
}


int main(void) {


    dict_store(tokens, machineCode);


    out = open(outputFile);
    input = open(inputFile);



    while(input -> currentLine != EOF) {
        

        while(currentToken != NULL) {

            currentToken = strtok(currentLine, " ");
            
            if(currentToken == NULL) {
                break;
            } else {

                machineCode = dict_get(currentToken);

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






