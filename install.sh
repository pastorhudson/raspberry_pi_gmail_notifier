sudo cp ./email-notifier.service /lib/systemd/system
sudo chmod 644 /lib/systemd/system/email-notifier.service
sudo systemctl daemon-reload
sudo systemctl enable email-notifier.service
sudo systemctl start email-notifier.service
sudo systemctl status email-notifier.service