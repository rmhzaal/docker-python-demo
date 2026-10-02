## Deployment

Deployed to a t3.micro EC2 instance (Ubuntu 22.04) to verify the image
runs identically outside the original build environment. Steps: installed
Docker on the instance, cloned this repo, built and ran the same
Dockerfile with no modifications, opened port 5000 in the security group,
and confirmed the app was reachable over the instance's public IP.

## Complete 
