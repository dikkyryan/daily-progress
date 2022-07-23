If you want to create Build definition for Angular project in Azure DevOps, then
this article is for you. Login to
<a href="https://dev.azure.com/" class="crayons-link">Dev Azure</a> and go to
the pipelines and follow the instructions below:

- Click on new pipeline ![](https://i.imgur.com/lL89yiV.png)

- Use classic editor ![](https://i.imgur.com/8wKAv3h.png)

- Connect to repo ![](https://i.imgur.com/q5iSJZO.png)

- Tag your repository on success ![](https://i.imgur.com/bS4MlDc.png)

- Install npm packages ![](https://i.imgur.com/qmxh1BG.png)

- Build angular project ![](https://i.imgur.com/AYjqRfy.png)

- Copy Files to staging directory ![](https://i.imgur.com/ZccWGkS.png)

- Archive Files ![](https://i.imgur.com/kVK0idi.png)

- Publish artifacts to Drop folder ![](https://i.imgur.com/wyaK8G1.png)

---

```yaml
pool:
  name: Azure Pipelines
  demands: npm

steps:
  - task: Npm@1
    displayName: 'npm install'
    inputs:
      verbose: false

  - task: Npm@1
    displayName: 'npm build'
    inputs:
      command: custom
      verbose: false
      customCommand: 'run build:apps'

  - task: CopyFiles@2
    displayName: 'Copy Files to: $(Build.ArtifactStagingDirectory)'
    inputs:
      SourceFolder: '$(Build.SourcesDirectory)/dist'
      TargetFolder: '$(Build.ArtifactStagingDirectory)'

  - task: ArchiveFiles@2
    displayName: 'Archive $(Build.ArtifactStagingDirectory)'
    inputs:
      rootFolderOrFile: '$(Build.ArtifactStagingDirectory)'
      includeRootFolder: false

  - task: PublishBuildArtifacts@1
    displayName: 'Publish Artifact: drop'
```

## Running Angular Build on Azure Devops

Once you run angular build on azure devops. Then you will see it will create a
job and execute all task mentioned in build definition.
![](https://i.imgur.com/F2mvHHa.png)

## Where Drop folder goes?

Final archived folder will go at
`$(System.DefaultWorkingDirectory)/$(Build.BuildId)` location.

Drop folder will have buildid.zip file inside that you will have both `apps` and
`libs` folders.

![](https://i.imgur.com/fk6r96i.png)

## What drop folder has?

Drop folder has both `apps` and `libs` folders.
![](https://i.imgur.com/OdEd027.png)