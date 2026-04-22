#!/bin/bash
echo "=== Loan Approval App - Deployment Script ==="
echo "Deployment started at: $(date)"

if [ ! -f "model.pkl" ]; then
    echo "ERROR: model.pkl not found. Run app.py first."
    exit 1
fi

mkdir -p build-output/tests/deploy
echo "Deployment directory created."

cp app.py build-output/tests/deploy/
cp predict.py build-output/tests/deploy/
cp model.pkl build-output/tests/deploy/
cp requirements.txt build-output/tests/deploy/

echo "Files copied to deployment directory."
echo "Application deployed successfully!"
echo "Deployment completed at: $(date)"