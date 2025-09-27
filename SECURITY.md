# Security Setup Guide

## Environment Variables Setup

### 🔒 **IMPORTANT: Never commit sensitive credentials to Git!**

### For Development:

1. **Copy the environment template:**

   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` with your values:**

   ```bash
   # Database Configuration
   POSTGRES_DB=py_init
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=your_secure_dev_password

   # Generate secure passwords using:
   openssl rand -base64 32
   # or
   python -c "import secrets; print(secrets.token_urlsafe(32))"
   ```

3. **Start the application:**
   ```bash
   make docker-dev
   ```

### For Production:

1. **Create `.env` with production values:**

   ```bash
   # Use STRONG passwords in production!
   POSTGRES_DB=py_init_prod
   POSTGRES_USER=app_user
   POSTGRES_PASSWORD=$(openssl rand -base64 32)
   ```

2. **Alternative: Use Docker secrets or external secret management**

### 🚨 **Security Checklist:**

- [ ] `.env` file is in `.gitignore`
- [ ] Strong passwords (min 20 characters)
- [ ] Different credentials for dev/staging/prod
- [ ] Environment variables used instead of hardcoded values
- [ ] Regular password rotation
- [ ] Consider using Docker secrets for production

### 🔐 **Password Generation:**

```bash
# Generate secure password
openssl rand -base64 32

# Or using Python
python -c "import secrets; print(secrets.token_urlsafe(32))"

# Or using uuidgen
uuidgen
```

### 📝 **Environment File Templates:**

#### Development (.env)

```bash
POSTGRES_DB=py_init
POSTGRES_USER=postgres
POSTGRES_PASSWORD=dev_secure_password_123
DEBUG=true
```

#### Production (.env)

```bash
POSTGRES_DB=py_init_prod
POSTGRES_USER=app_prod_user
POSTGRES_PASSWORD=STRONG_PROD_PASSWORD_HERE
DEBUG=false
```

### 🛡️ **Best Practices:**

1. **Never share `.env` files** in chat, email, or documentation
2. **Use different passwords** for each environment
3. **Rotate passwords regularly** (quarterly recommended)
4. **Use secrets management** for production (AWS Secrets Manager, HashiCorp Vault, etc.)
5. **Enable 2FA** on database access where possible
6. **Monitor access logs** regularly

### 🔧 **For CI/CD:**

Set environment variables in your CI/CD platform:

- GitHub Actions: Repository Secrets
- GitLab CI: Variables (masked)
- Jenkins: Credentials Plugin
- Docker Swarm: Docker Secrets
