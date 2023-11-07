module.exports = {
  apps: [
    {
      name: "my-django-project",
      script: "./manage.py",
      args: ["runserver"],
      exec_mode: "fork",
      instances: 1,
      watch: false,
      autorestart: true,
      max_restarts: 5,
      interpreter: "python",
    },
  ],
};
