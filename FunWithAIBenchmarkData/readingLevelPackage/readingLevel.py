# File Name: readingLevel.py
# Student Name: Nate Hoang, Andrew Rozsits, Ray Happel
# email:  hoangnbd@mail.uc.edu, rozsitaj@mailk.uc.edu, happelrc@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   3/26
# Course #/Section:   4010-001
# Semester/Year:   Spring 25
# Brief Description of the assignment:  Using github and working as a group to produce an image and a cool visual design

# Brief Description of what this module does. This module links our python to data sets to produce visuals
# Citations: Chatgpt, https://www.w3schools.com/, gemini

# Anything else that's relevant:

import contextlib
import textstat
from utilitiesPackage.utilities import *

class Reading_Level:
    """
    Utilities to compute reading level data for text strings
    """
    @staticmethod 
    def compute_readability_indices(benchmark_name, text):
        """
        This method computes several readability indices for a given text string.
        @param benchmark_name String: The name of the benchmark, which may be used in a file path when the indicies are written to disk.
        @param text String: The text string to analyze.

        @returns dictionary:
            A dictionary containing the following readability indices (dictionary keys):
                - Flesch-Kincaid Grade (Flesch-Kincaid Grade)
                - Flesch-Kincaid Reading Ease Score (Flesch-Kincaid Reading Ease)
                - Gunning Fog Index (GunningFog)
                - Coleman-Liau Index (ColemanLiau)
                - Automated Readability Index (ARI)
                - SMOG Index (SMOG)
                - LIX (LIX)
        """
        results = {}
        results["Flesch-Kincaid Grade"] = textstat.flesch_kincaid_grade(text)
        results["Flesch-Kincaid Reading Ease"] = textstat.flesch_reading_ease(text)
        results["GunningFog"] = textstat.gunning_fog(text)
        results["ColemanLiau"] = textstat.coleman_liau_index(text)
        results["ARI"] = textstat.automated_readability_index(text)
        results["SMOG"] = textstat.smog_index(text)
        results["LIX"] = textstat.lix(text)

        #print("********************* writing reading levels ********************")
        write_dict_to_file(results, ".\\dataPackage\\" + benchmark_name + "\\results\\reading_level.txt", 0)

        return results

    @staticmethod 
    def test01():
        """
        Compute the readability indices of a paragraph that is rewritten in progressively simpler language. 
        Start at grad school level (?) and rewrite it to simplify down to words with 4 letters or less. 
        """
        text = """
        The burgeoning field of machine learning has become a potent elixir for astronomers drowning in a sea of data.\
        These sophisticated algorithms act as celestial sieves, meticulously sifting through the ever-expanding deluge\
        of information gleaned from powerful telescopes and spacefaring missions. By discerning subtle stellar whispers\
        and cosmic correlations that would elude even the most discerning human gaze, machine learning is accelerating \
        our quest to unravel the enigmatic tapestry of the cosmos. For instance, these algorithms are transforming \
        the way we classify galaxies, achieving a level of taxonomic precision previously unimaginable. \
        This newfound acuity is leading to groundbreaking revelations concerning galactic genesis and evolution. \
        As these tools continue to be honed and refined, their transformative impact on astronomy promises to propel us \
        towards an even deeper understanding of the universe's grand design.
        """
        # There are excess blanks, just to make the code above more readable. We can remove them now.
        for i in range(0,10):
            text = text.replace("  "," ")
        print(text)

        ri = Reading_Level.compute_readability_indices("Dummy Benchmark", text)
        for key in ri.keys():
            print(key, ":", ri[key])
        print("=======================")

        text = """
                  Look! Space scientists have cool helpers called machines that learn.\
                  These machines help them look at all the new pictures from space telescopes, \
                  like looking for toys in a giant box. \
                  The machines are good at finding things people might miss, \
                  like special shapes in the stars. \
                  This helps scientists learn more about space, like how stars are born and grow up! \
                  Just like you learn new things, the machines are getting smarter too, \
                  so they can help us discover even more amazing things in space!
               """
        # There are excess blanks, just to make the code above more readable. We can remove them now.
        for i in range(0,10):
            text = text.replace("  "," ")
        print(text)

        ri = Reading_Level.compute_readability_indices("Dummy Benchmark", text)
        for key in ri.keys():
            print(key, ":", ri[key])
        print("=======================")

        text = """
               Scientists see lots of space pictures! \
               They use special machines to help them look. \
               The machines are good at finding things that scientists might miss, like sparkly stars. \
               This helps scientists learn more about space, like where stars come from! \
               The machines are getting smarter to help us find even more cool things in space!
               """
        # There are excess blanks, just to make the code above more readable. We can remove them now.
        for i in range(0,10):
            text = text.replace("  "," ")
        print(text)

        ri = Reading_Level.compute_readability_indices("Dummy Benckmark", text)
        for key in ri.keys():
            print(key, ":", ri[key])
        print("=======================")

        text = """
               See space pics! Fun machines help look! Find cool stars! Learn more space! Stars go boom! Smart machines find more!
               """
        # There are excess blanks, just to make the code above more readable. We can remove them now.
        for i in range(0,10):
            text = text.replace("  "," ")
        print(text)
        ri = Reading_Level.compute_readability_indices("Dummy Benchmark", text)
        for key in ri.keys():
            print(key, ":", ri[key])
