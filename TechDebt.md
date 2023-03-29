# Technical Debt
## CI Tool
We decide to use `pylint` as our CI tool for this project. Pylint is a static code checker, meaning it can analyse your code without actually running it. Pylint checks for errors, tries to enforce a coding standard, and tries to enforce a coding style.

Right after added `pylint`, we got two errors:
```
hello_world.py:1:0: C0304: Final newline missing (missing-final-newline)
hello_world.py:1:0: C0114: Missing module docstring (missing-module-docstring)
```
Those two error are from `hello_world.py` file. With a little research, we find out what those errors means.
The first warning, C0304, is indicating that there is no final newline at the end of your file. It is recommended to add a final newline at the end of your file to avoid issues with some programs that expect files to end with a newline character.

The second warning, C0114, is indicating that there is no module docstring in your code. A docstring is a string that appears at the beginning of a module, class, or function and provides documentation about what the code does. It is good practice to include a docstring to help other developers understand the purpose and usage of your code.

After fixing those two errors, we got the green check for this project. 

**Here are the screenshots of our machine with working projects:**

Gafur

![image](https://user-images.githubusercontent.com/101157079/227807836-91ae5935-dfe7-4e31-af19-f9b22e96e9b8.png)

Sophie

![image](https://user-images.githubusercontent.com/101157079/227807937-476fb9dc-b6a5-4647-a32f-56c43f92b7e2.png)

Calvin

![image](https://user-images.githubusercontent.com/101157079/227807901-25d9337d-7293-4a0c-ae50-248048176fcf.png)

Ryan

![image](https://user-images.githubusercontent.com/101157079/227853786-356ed51a-c0cb-4ed1-af16-e5334c32de90.png)
