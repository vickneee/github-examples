# SSH Key in GitHub

1. Open Terminal.

2. Enter the following command to generate a new SSH key. Replace `your_email@example.com` with your GitHub email address.

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

3. When you're prompted to "Enter a file in which to save the key," press Enter. This accepts the default file location.

4. At the prompt, type a secure passphrase.

5. Now, you need to add the SSH key to your GitHub account. First, copy the SSH key to your clipboard.

```bash
cat /Users/victoriavavulina/.ssh/id_ed25519.pub
```

You will be able to copy the public key in OpenSSH format which you can then add to your GitHub account.

6. Go to your GitHub account and click on your profile icon in the top right corner. Then, click on Settings.

7. In the user settings sidebar, click on SSH and GPG keys.

8. Click on New SSH key.

9. In the "Title" field, add a descriptive label for the new key.

10. Paste your key into the "Key" field.

11. Click Add SSH key.

12. If prompted, confirm your GitHub password.

13. You're all set! You can now use SSH to interact with GitHub repositories.
