Steps to use:
1. Pull the repository.
2. Build the image by running: ``` docker build html_analyzer:latest . ```
3. Write your letter and save it in 'aa_exercise/letter' as a txt file.
4.1. If the magazine article is in txt file, then copy it to 'aa_exercise/magazine_article/' as a txt file.
4.2. If the magazine article is in html file, then copy the link in your clipboard (cmd + c or ctrl + c).
5. Run: ``` docker run -a stdout -it -v `pwd`:/app html_analyzer:latest ```
6. Choose html or txt.
7. Find out if it's doable.

Disclaimer:
Keep in mind that we're just considering aplhanumeric characters in order to know if we can write the letter.
