# GHA-RUNNER

```
export RUNNER_TOKEN=AB5*******************

helm upgrade --install --atomic \
    --create-namespace  \
    --namespace gha-runner  \
    --set image.tag=latest \
    --set env[1].name=RUNNER_TOKEN --set env[1].value=$RUNNER_TOKEN \
    -f apps/gha-runner/.helm/values.yaml -f apps/gha-runner/.helm/sandbox/values.yaml \
    gha-runner .helm-tmpl  
    
```