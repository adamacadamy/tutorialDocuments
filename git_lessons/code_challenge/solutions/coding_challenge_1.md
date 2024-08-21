# GitHub & Git Challenge

## Challenge Overview

You will complete a series of tasks that simulate common GitHub and Git operations. These tasks include creating a repository, managing branches, committing changes, and collaborating with others. Follow the steps below carefully.

## Steps to Complete the Challenge

1. **Create a New GitHub Repository**

   - Go to [GitHub](https://github.com/) and sign in to your account.
   - Create a new repository with the name `git-collaboration`.
   - Initialize the repository with a `README.md` file if desired.
2. **Clone the Repository to Your Local Machine**

   - Copy the repository URL from the GitHub page.
   - Open your terminal or command prompt and execute the following command:
     ```bash
     git clone <repository-url>
     ```
   - Replace `<repository-url>` with the URL you copied.
3. **Create a New Branch Named `feat/lorem_ipsum`**

   - Navigate to the directory of your cloned repository:
     ```bash
     cd git-collaboration
     ```
   - Create a new branch and switch to it:
     ```bash
     git checkout -b feat/lorem_ipsum
     ```
4. **Add a `lorem_ipsum.md` Markdown File with Lorem Ipsum Text**

   - Create a new file named `lorem_ipsum.md` in the repository's root directory.
   - Add the following content:
     ```markdown
     # Lorem Ipsum Text

     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada.
     ```
5. **Stage the File for Commit**

   - Stage the `lorem_ipsum.md` file:
     ```bash
     git add lorem_ipsum.md
     ```
6. **Commit the Changes**

   - Commit your staged changes with the commit message "add lorem ipsum":
     ```bash
     git commit -m "add lorem ipsum"
     ```
7. **Push the Changes to the Remote Repository**

   - Push your `feat/lorem_ipsum` branch to the remote GitHub repository:
     ```bash
     git push origin feat/lorem_ipsum
     ```
8. **Add a Collaborator Named "fuzumoe"**

   - On GitHub, go to the repository's "Settings".
   - Select "Collaborators" from the left sidebar.
   - Invite the user `fuzumoe` as a collaborator to the repository. You may need to wait for them to accept the invitation.
9. **Create a Pull Request (PR)**

   - After pushing your branch, go to the "Pull Requests" tab on the GitHub repository page.
   - Create a new pull request (PR) from the `feat/lorem_ipsum` branch into the `main` branch.
   - In the pull request, assign `fuzumoe` as a reviewer.

## Additional Notes

- Be sure to include a descriptive title and summary for your pull request.
- Review your changes before submitting the pull request to ensure everything is correct.
- After the pull request is reviewed, you can choose to merge it.

## Expected Outcome

You should complete the following:

- A new branch with a `lorem_ipsum.md` file committed.
- A successfully created pull request.
- Collaboration with the user `fuzumoe` as a collaborator and reviewer.

Good luck and happy coding!
