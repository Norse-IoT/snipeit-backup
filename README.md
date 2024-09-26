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

You should then create a Personal Access Token for yourself, and store it as `SNIPEIT_TOKEN` in your `.env` file.

This token should last ~15 years. It will be the automated way to backup file content.

Be careful not to leak it.

## Crontab

We need a crontab on the server to make regular backups:

```bash
$ crontab -e
```

You can checkout <https://crontab-generator.org/> for more info.

Here's the crontab I used to backup every two days at 4am:

We anticipate that nobody is going to be logging new stuff at exactly 4am.

```cron
0 4 1-31/2 * * /usr/bin/php /var/www/html/snipeit/artisan snipeit:backup > /var/log/snipeit-backup.log
```

These backups will then be downloaded by our download script.

# venv

It is expected to use this project with [a Python virtual environment](https://docs.python.org/3/library/venv.html).

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

On the machine I want to download the backups to, I've added this crontab:

```cron
* */12 * * * /home/iplus/snipeit-backup/venv/bin/python3 /home/iplus/snipeit-backup/backup.py > /var/log/snipeit-backup.log
```

