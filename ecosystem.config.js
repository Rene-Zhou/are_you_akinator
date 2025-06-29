module.exports = {
  apps: [
    {
      name: 'akinator-backend',
      script: 'uv',
      args: 'run python run_backend.py',
      cwd: '/home/rene/dev/are_you_akinator',
      instances: 1,
      autorestart: true,
      watch: false,
      max_memory_restart: '500M',
      env: {
        NODE_ENV: 'production',
        PORT: 8000
      },
      env_development: {
        NODE_ENV: 'development',
        PORT: 8000
      },
      log_file: './logs/backend.log',
      out_file: './logs/backend-out.log',
      error_file: './logs/backend-error.log',
      time: true
    },
    {
      name: 'akinator-frontend',
      script: 'npm',
      args: 'run dev',
      cwd: '/home/rene/dev/are_you_akinator/frontend',
      instances: 1,
      autorestart: true,
      watch: false,
      max_memory_restart: '300M',
      env: {
        NODE_ENV: 'production',
        PORT: 3000
      },
      env_development: {
        NODE_ENV: 'development',
        PORT: 3000
      },
      log_file: './logs/frontend.log',
      out_file: './logs/frontend-out.log',
      error_file: './logs/frontend-error.log',
      time: true
    }
  ]
};