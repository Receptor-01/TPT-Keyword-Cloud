# Word Cloud Generator

This repository contains a simple Python script (**cloud-script.py**) that generates a word cloud image from the names of TPT products listed in a CSV file.

---

## Overview

**cloud-script.py** reads data from a Teachers Pay Teachers product statistics CSV that you will need to rename to **`product-stats.csv`**, then looks at all the keywords used in your product titles, and generates a word cloud image with the most commonly occuring keywords. (named **`WORD-CLOUD.jpg`** by default).  

This word cloud allows you to see the range of keywords used in your product titles, and get a visual gauge of the relative prevalance of each. 

### Key Features

- **Stopwords Removal**: Removes common English stopwords plus a custom set of stopwords to omit and keep keywords relevant. (Took out words like 'activity', 'worksheet', 'grade' as these likely appear in many product titles)

- **Word Cloud Generation**: Uses the [WordCloud](https://pypi.org/project/wordcloud/) library to visualize the most frequent words.  

- **Output Format**: The script saves the output as a **`.jpg`** file to maintain a relatively small file size.  

---

## Prerequisites & Dependencies

1. **Python 3**  
   - If you have Python 3 installed, ensure you know your environment path.  
   - Example: `/opt/homebrew/bin/python3` or `python3` on many systems.

2. **Pandas**  
   ```bash
   pip install pandas

   ```bash

   pip install matplotlib

   pip install wordcloud

   pip install nltk

   python -m nltk.downloader stopwords


# Running The Script

3. Copy or place your CSV file (product-stats.csv) in the same directory as cloud-script.py.

4. Open your terminal (or command prompt) and navigate to the folder containing cloud-script.py.

5. Run the script: 

  ```bash
   python cloud-script.py


5. Check for the generated file:
 - A new file named WORD-CLOUD.jpg should appear in the same directory.
 - Open it to verify it contains a word cloud image.


Configuration
 - CSV Path: By default, the expected CSV file name is set to **product-stats.csv**. It's recommended to simply change the CSV file name of your product-stats download, but you can also edit this at the top of cloud-script.py if you want your CSV named differently.

 - Output Image Path: By default, output_image_path is WORD-CLOUD.jpg. You can also change this if you prefer a different filename or file path.

Contributing
 - Feel free to open an issue or submit a pull request if you have suggestions to improve functionality or clarity.



