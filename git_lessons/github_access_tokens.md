# GitHub personal access token
Steps to generate and use GitHub personal access token are given here in brief.
 
###  Generate
1. #### Go to your GitHub profile page, `https://github.com/<username>`.  
![alt text](images/user_page.png)

2. #### Click on the avatar icon on the top right corner.
![alt text](images/right_corner.png)

3. #### Scroll down to have Developer settings on the left.
![alt text](images/developer_setting.png)

4. #### Click Developer settings
![alt text](images/access_token_info.png)

5. #### Expand Personal access tokens and choose Tokens (classic).
![alt text](images/classic_token.png)

6. #### Click Generate new token button on the right.
![alt text](images/generate_token.png)

7. ### Confirm access.
![alt text](images/confirm_with_out.png)


8. #### Fill Note field to remind you the purpose of this token, e.g. lecture-notes.
![alt text](images/token_note.png)

9. #### Click Generate token button.
![alt text](images/generate_token_button.png)

10. #### CPersonal access token is created. Save it since it will not display again. Refresh the page.
![alt text](images/personal_token_created.png)
 
11. #### Personal access token is created. Save it since it will not display again. Refresh the page.

![alt text](images/save_token.png)

12. #### To enable Git's credential store, run the following command in your terminal:

```bash
git config --global credential.helper store
```