# GitHub & Git Coding Challenge

## Instructions

1. **Create a GitHub Repository**  
   - Log in to your GitHub account.
   - Create a new repository named `lorem-ipsum-repo`. Make it either public or private, depending on your preference.

2. **Clone the Repository to Your Local Machine**  
   - On your GitHub repository page, click the green "Code" button and copy the HTTPS or SSH URL.
   - Open your terminal and clone the repository:
     ```bash
     git clone <repository-url>
     ```
   - Replace `<repository-url>` with the URL you copied from GitHub.

3. **Create a New Branch Named `feat/lorem_ipsum`**  
   - Navigate to the cloned repository on your local machine:
     ```bash
     cd lorem-ipsum-repo
     ```
   - Create and switch to the new branch:
     ```bash
     git checkout -b feat/lorem_ipsum
     ```

4. **Add a Markdown File with Lorem Ipsum Text**  
   - Create a new file called `lorem_ipsum.md` in the repository.
   - Add the following Lorem Ipsum text to the file:
     ```markdown
     # Lorem Ipsum

     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
     ```
   - Save the file.

5. **Stage the File**  
   - Stage the new file:
     ```bash
     git add lorem_ipsum.md
     ```

6. **Commit the Changes**  
   - Commit the changes with the message `"add lorem ipsum"`:
     ```bash
     git commit -m "add lorem ipsum"
     ```

7. **Push the Changes to the Remote Repository**  
   - Push your branch to the remote repository:
     ```bash
     git push origin feat/lorem_ipsum
     ```

8. **Add User "fuzumoe" as a Collaborator**  
   - Go to the "Settings" tab of your repository on GitHub.
   - Select "Collaborators" from the left sidebar.
   - Add the user `fuzumoe` as a collaborator to the repository.

9. **Create a Pull Request (PR) for the `feat/lorem_ipsum` Branch**
   - On the GitHub repository page, click "Pull requests" and create a new pull request.
   - Select `feat/lorem_ipsum` as the branch to merge into `main`.
   - Add the user `fuzumoe` as a reviewer for the pull request.
   - Submit the pull request.

## Expected Outcome
By the end of this challenge, you should have:
- A repository with a `lorem_ipsum.md` file on a new branch.
- A successfully created pull request with user `fuzumoe` as a reviewer.
- Proper GitHub collaboration set up with user `fuzumoe`.

Good luck!
