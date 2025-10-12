# Deployment Checklist for Koyeb

Use this checklist when deploying APIIngest to Koyeb.

## 📋 Pre-Deployment

- [ ] Code is committed and pushed to GitHub
- [ ] All tests pass locally
- [ ] Environment variables documented
- [ ] `.env.example` files created

## 🔧 Backend Service Setup

### Basic Configuration
- [ ] Service name: `apiingest-backend`
- [ ] Repository connected
- [ ] Working directory: `backend`
- [ ] Build method: Buildpack (or Dockerfile)
- [ ] Port: `8000`

### Build Settings
- [ ] Build command: (leave empty for buildpack)
- [ ] Run command: `uvicorn main:app --host 0.0.0.0 --port 8000`

### Environment Variables
- [ ] `ALLOWED_ORIGINS` = `https://your-frontend-url.koyeb.app` (update after frontend deploy)
- [ ] `PORT` = `8000`

### Health Check
- [ ] Path: `/health`
- [ ] Port: `8000`
- [ ] Grace period: 30s
- [ ] Interval: 30s

### Deployment
- [ ] Click "Deploy"
- [ ] Wait for build to complete
- [ ] Note backend URL: `https://apiingest-backend-xxx.koyeb.app`
- [ ] Test health endpoint: `curl https://your-backend-url/health`

## 🎨 Frontend Service Setup

### Basic Configuration
- [ ] Service name: `apiingest-frontend`
- [ ] Repository connected
- [ ] Working directory: `frontend`
- [ ] Build method: Buildpack
- [ ] Port: `3000`

### Build Settings
- [ ] Build command: `npm install && npm run build`
- [ ] Run command: `npm start`

### Environment Variables
- [ ] `NEXT_PUBLIC_API_URL` = `https://apiingest-backend-xxx.koyeb.app` (from step 1)
- [ ] `NODE_ENV` = `production`

### Deployment
- [ ] Click "Deploy"
- [ ] Wait for build to complete
- [ ] Note frontend URL: `https://apiingest-frontend-xxx.koyeb.app`
- [ ] Test frontend: Open URL in browser

## 🔄 Post-Deployment Configuration

### Update CORS
- [ ] Go to backend service settings
- [ ] Update `ALLOWED_ORIGINS` environment variable
- [ ] Value: `https://apiingest-frontend-xxx.koyeb.app` (your actual frontend URL)
- [ ] Redeploy backend service

### Test Integration
- [ ] Open frontend URL
- [ ] Upload example file from `examples/`
- [ ] Verify conversion works
- [ ] Check downloaded markdown file
- [ ] Test error handling (invalid file)

## 🌐 Custom Domain (Optional)

### Backend Domain
- [ ] Go to backend service → Domains
- [ ] Add custom domain (e.g., `api.yourdomain.com`)
- [ ] Update DNS records as instructed
- [ ] Wait for DNS propagation
- [ ] Update frontend's `NEXT_PUBLIC_API_URL`
- [ ] Update backend's `ALLOWED_ORIGINS`

### Frontend Domain
- [ ] Go to frontend service → Domains
- [ ] Add custom domain (e.g., `yourdomain.com`)
- [ ] Update DNS records as instructed
- [ ] Wait for DNS propagation
- [ ] Update backend's `ALLOWED_ORIGINS`

## 🔍 Verification

### Backend Checks
- [ ] Health endpoint responds: `GET /health`
- [ ] API docs accessible: `GET /docs`
- [ ] CORS headers present in responses
- [ ] File upload works: `POST /convert`

### Frontend Checks
- [ ] Homepage loads correctly
- [ ] File upload interface works
- [ ] Drag and drop functions
- [ ] Error messages display properly
- [ ] Success notifications appear
- [ ] File downloads automatically
- [ ] Dark mode toggles correctly

### Integration Checks
- [ ] Frontend can reach backend
- [ ] CORS errors don't appear in console
- [ ] File conversion completes successfully
- [ ] Downloaded file is valid markdown
- [ ] Error handling works correctly

## 📊 Monitoring Setup

- [ ] Check deployment logs for errors
- [ ] Monitor CPU/memory usage
- [ ] Set up alerts (if available)
- [ ] Test health check endpoints
- [ ] Verify auto-restart on failure

## 🔐 Security Review

- [ ] HTTPS enabled (automatic with Koyeb)
- [ ] CORS restricted to specific origins
- [ ] No sensitive data in logs
- [ ] Environment variables not exposed
- [ ] File uploads validated
- [ ] Temporary files cleaned up

## 📝 Documentation

- [ ] Update README with deployment URLs
- [ ] Document environment variables used
- [ ] Note any deployment-specific configuration
- [ ] Update CHANGELOG with deployment info

## 🎉 Launch

- [ ] Share frontend URL with users
- [ ] Monitor for issues
- [ ] Gather user feedback
- [ ] Plan improvements

## 📞 Troubleshooting

### Common Issues

**CORS Errors**
- Verify `ALLOWED_ORIGINS` includes frontend URL
- No trailing slashes in URLs
- Redeploy backend after changing env vars

**Build Failures**
- Check build logs in Koyeb dashboard
- Verify `package.json` has `build` and `start` scripts
- Ensure all dependencies in `requirements.txt`

**Connection Refused**
- Verify `NEXT_PUBLIC_API_URL` is correct
- Check backend service is running
- Test backend health endpoint directly

**404 Errors**
- Verify working directory is correct
- Check file paths in run commands
- Ensure build output is in correct location

## 🔄 Redeployment

When making updates:
- [ ] Commit and push changes to GitHub
- [ ] Koyeb auto-deploys (if configured)
- [ ] OR manually trigger deployment
- [ ] Verify changes in production
- [ ] Test all functionality
- [ ] Monitor logs for errors

## ✅ Deployment Complete!

Once all items are checked:
- 🎉 Your application is live!
- 📊 Monitor the deployment
- 🐛 Watch for any issues
- 💬 Gather user feedback
- 🚀 Plan next features

---

**Deployment Documentation:** See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for detailed instructions.

**Need Help?** Check logs in Koyeb dashboard or refer to troubleshooting section above.

