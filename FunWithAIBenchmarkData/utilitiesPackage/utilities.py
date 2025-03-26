# utilities.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os



def display_team_logo(image_path="images/golbat.png"):
    """
    Displays the team logo image (e.g., Golbat) using matplotlib.
    Parameters:image_path (str): Relative or absolute path to the image file.
    Returns:If the image file exists, it will be displayed in a 200x200 pixel window (roughly). 
            If none Returns: Image not found at {image_path}
    """
    if os.path.exists(image_path):
            img = mpimg.imread(image_path)
            plt.figure(figsize=(2, 2))  # Roughly 200x200 pixels at 100 dpi
            plt.imshow(img)
            plt.axis('off')
            plt.title("Team Golbat", fontsize=10)
            plt.show()
    else:
            print(f"Image not found at: {image_path}")
        



"""
    def write_questions_to_text_files(benchmark_name, questions):
        
        Write the questions and all possible answers to one text file.
        Write the correct answers to another text file.
        @param benchmark_name String: the name to use when creating the text files. Will also be used to build a file path into the data package.
        @param questions list: List of dictionaries . The following key/value pairs are expected in each dictionary: 
                                                               "prompt" (value = string)
                                                               "possible answers" (value = list of strings)
                                                               "correct answer" (value = string). 
        @return int: count of questions written to the text files
        
    
        # If the path does not exist, build it
        path = "./dataPackage/" + benchmark_name + "/"
        if not os.path.exists(path):
            os.makedirs(path)
        path = "./dataPackage/" + benchmark_name + "/results/"
        if not os.path.exists(path):
            os.makedirs(path)
    
        # Process the questions and write the CSV files
        question_file_name = path + benchmark_name + "_questions_and_answers.txt"
        answer_file_name = path + benchmark_name + "_correct_answers.txt"
        count = 0
        with open(question_file_name, 'w', encoding='utf-8') as question_file:
            with open(answer_file_name, 'w', encoding='utf-8') as answer_file:
                for question in questions:
                    text = question["question id"] + "," + question["prompt"] + "," + ', '.join(str(answer) for answer in question["possible answers"]) + "\n"
                    question_file.write(text)
                    text = question["question id"] + "," + question["correct answer"] + "\n"
                    answer_file.write(text)
                    count += 1
        return count

    def convert_dictionaries_to_string(questions, keys = None):
        
        Process a list of dictionaries into one big honking text string
        @param questions list: The list of dictionaries to be processed. 
        @param keys list: a list of keys to be processed for each dictionary in questions. If None, all keys will be processed. Defaults to None
        @return String: a long text string, the values associated with the keys in all the dictionaries concatenated together.
        
        text = ""
        if keys == None:
            for question in questions:
                for key in question.keys():
                    value = question[key]
                    if isinstance(value, (list, tuple, set)):
                        for item in value:
                            text += " " + item
                    else:
                        text += " " + value
        else:
            for question in questions:
                for key in keys:
                    value = question[key]
                    if isinstance(value, (list, tuple, set)):
                        for item in value:
                            text += " " + item
                    else:
                        text += " " + value
        return text

    def read_directory_contents(path):
        
        Read the contents of a directory
        @param path String: the path of the directory to be processed
        @return: a list
        
        # Get list of contents in the folder
        contents = os.listdir(path)
        return contents

    def write_string_to_file(text, file_name):
        
        Writes a string to a file.

        @param text string: The string to write.
        @param file_name: The name of the file to write to.
        @return bool: True if file was written, False if an exception was thrown
        
 
        status = True
        try:
            # Create the directory if it doesn't exist
            os.makedirs(os.path.dirname(file_name), exist_ok=True)

            # Open the file in write mode  
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(text)
            #print(f"String written to file: {filename}")
        
        except Exception as e:
            status = False
            print(f"Utilities.write_string_to_file(): Error writing to {file_name}: {e}")
        
        return status

    def write_dict_keys_to_file(dictionary, file_name, length = 0):
        
        Writes the keys of a dictionary to a text file, one per line.

        @param dictionary dict: The dictionary whose keys will be written.
        @param filename string: The name of the file to write to.
        @return bool: True if file was written, False if an exception was thrown
        
 
        status = True
        try:
            with open(file_name, 'w', encoding='utf-8') as f:
                if length == 0:
                    for key in dictionary:
                        f.write(str(key) + '\n')
                else:
                    #print("Writing", length, "words to file.")
                    for key in list(dictionary.keys())[0:length]:
                        f.write(str(key) + '\n')
                
        except Exception as e:
            status = False
            print(f"Utilities.write_dict_keys_to_file(): Error writing to {file_name}: {e}")
        
        return status

    def write_dict_to_file(dictionary, file_name, length = 0, denominator = 0):
        
        Writes the keys and values of a dictionary to a text file, one per line.

        @param dictionary dict: The dictionary whose keys will be written.
        @param file_name string: The name of the file to write to.
        @param length int: The number of key/value pairs to write. If 0, write all. Defaults to zero
        @param denominator int: The number to use for the denominator when calculating percentages. Defaults to 0 and no perecentages will be calculated.
        @return bool: True if file was written, False if an exception was thrown
        

        status = True
        try:
            with open(file_name, 'w', encoding='utf-8') as f:
                if length == 0:
                    #print("write_dict_to_file length = 0", "********************* writing", len(dictionary), "dictionary items to", file_name, " ********************")
                    for key in dictionary:
                        if denominator == 0:
                            f.write(str(key) + ": " + str(dictionary[key]) + '\n')
                        else:
                            f.write(str(key) + ": " + str(dictionary[key]) + ", " + '{0:.2f}'.format((dictionary[key] / denominator) * 100) + '\n')
                else:
                    #print("write_dict_to_file", "********************* writing", length, "dictionary items to", file_name, " ********************")
                    for key in list(dictionary.keys())[0:length]:
                        if denominator == 0:
                            f.write(str(key) + ": " + str(dictionary[key]) + '\n')
                        else:
                            f.write(str(key) + ": " + str(dictionary[key]) + ", " + '{0:.2f}'.format((dictionary[key] / denominator) * 100) + '\n')
        except Exception as e:
            status = False
            print(f"Utilities.write_dict_to_file(): Error writing to {file_name}: {e}")
"""    



