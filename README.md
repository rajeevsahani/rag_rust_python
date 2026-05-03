# Create README
echo "# rag_rust_python" >> README.md

# Initialize git repo
git init

# Stage and commit
git add README.md
git commit -m "first commit"

# Set main branch
git branch -M main

# Add remote repository
git remote add origin https://github.com/rajeevsahani/rag_rust_python.git

# Push to GitHub
git push -u origin main