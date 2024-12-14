[Unit]
Description=Gunicorn instance to serve Django project
After=network.target

[Service]
User=user-name
Group=group-name
WorkingDirectory=/chatbot/ci-cd-configurations-file/shakti
ExecStart=/chatbot/ci-cd-configurations-file/shakti/gunicorn --workers 3 --bind 0.0.0.0:8000 shakti.wsgi:application
Restart=always
[Install]
WantedBy=multi-user.target
~                                
