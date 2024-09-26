# snipeit-backup

For context, Tyler installed snipeit on a raspberry pi to act as our asset manager.

# Backups 

We can run:

```bash
/usr/bin/php /var/www/html/snipeit/artisan snipeit:backup
```

to create a backup on the pi.

To download the backup onto another machine, we can use the [backups](https://snipe-it.readme.io/reference/backups-1) API.

To access this API, you must create a user in SnipeIt that [has the superuser](https://github.com/snipe/snipe-it/blob/6c85ba3495a005be6a413e014c51b25a820db31a/routes/web.php#L180) entitlement.

You should then create a Personal Access Token for yourself, and store it as TOKEN in your `.env` file.

This should last ~15 years. It will be the automated way to backup file content.

Be careful not to leak it.

## Crontab

We need a crontab on the server to make regular backups:

```bash
$ crontab -e
```

You can checkout <https://crontab-generator.org/> for more info.





