# Koyeb Configuration Quick Reference

Use this as a cheat sheet when filling out the Koyeb deployment form.

## 🎯 Single-Service Deployment

### Section 1: Service Type
- ✅ **Web service**

### Section 2: Source
- **Repository**: `mohidbt/apic` (or your repo)
- **Branch**: `main`

### Section 3: Builder (+3)
- **Build method**: ✅ **Dockerfile**
- **Dockerfile location**: *(leave empty)* - uses root `Dockerfile`
- **Work directory**: *(leave empty)*
- **Entrypoint**: *(leave empty)*
- **Command**: *(leave empty)*
- **Target**: *(leave empty)*

### Section 4: Environment Variables (+4)

Click **+ Add another** for each:

```
Name: PORT
Value: 8000

Name: ALLOWED_ORIGINS
Value: https://{{ KOYEB_PUBLIC_DOMAIN }}/,http://localhost:3000

Name: NEXT_PUBLIC_API_URL
Value: http://localhost:8000

Name: NODE_ENV
Value: production
```

### Section 5: Instance (+5)
- **Instance type**: Free (0.1 vCPU, 512MB RAM, 2000MB Disk)
- **Region**: Frankfurt 🇩🇪 (or your preferred region)

### Section 6: Scaling (+6)
- **Autoscaling**: 0-1 instances/region *(default)*

### Section 7: Volumes (+7)
- **Volumes**: No volumes configured *(default)*

### Section 8: Ports (+8)
- **Port**: `8000`
- **Protocol**: HTTP
- Should show: **1 configured** ✅

### Section 9: Health Checks (+9)
- **Type**: TCP health check on port 8000 *(auto-configured)*
- Or HTTP check on `/health` endpoint

### Section 0: Service Name
- **Name**: `apiingest` (or your preferred name)

---

## 📋 Copy-Paste Environment Variables

For quick copy-paste into Koyeb:

```bash
PORT=8000
ALLOWED_ORIGINS=https://{{ KOYEB_PUBLIC_DOMAIN }}/,http://localhost:3000
NEXT_PUBLIC_API_URL=http://localhost:8000
NODE_ENV=production
```

---

## ✅ Pre-Deployment Checklist

- [ ] Root `Dockerfile` exists in repository
- [ ] `supervisord.conf` exists in repository
- [ ] `start.sh` exists in repository
- [ ] Repository connected to Koyeb
- [ ] Branch selected: `main`
- [ ] Builder: Dockerfile ✅
- [ ] All 4 environment variables added
- [ ] Port set to 8000
- [ ] Health check configured

---

## 🚀 Deploy Button

Once all sections are filled:
1. Review configuration
2. Click **Deploy** button
3. Wait 3-5 minutes for build
4. Check logs if build fails
5. Access service at: `https://your-service-name.koyeb.app`

---

## 🔍 Post-Deployment

Test your deployment:

```bash
# Test backend health
curl https://your-service.koyeb.app/health

# Test frontend (if reverse proxy configured)
curl https://your-service.koyeb.app/
```

---

## ⚠️ Common Issues

| Issue | Solution |
|-------|----------|
| Build fails | Check `Dockerfile` syntax, verify all dependencies |
| Service won't start | Check logs, verify supervisord config |
| 502 Bad Gateway | Service still starting, wait 1-2 minutes |
| CORS errors | Update `ALLOWED_ORIGINS` with actual domain |
| Frontend not loading | Port 3000 not exposed, need reverse proxy in backend |

---

For detailed troubleshooting, see [KOYEB_SINGLE_SERVICE.md](KOYEB_SINGLE_SERVICE.md)

