# Deploy key

<style>
input {
    border-style: none;
    display: inline-block;
    background-color: #191919;
    min-width: 154px;
    font-size: 16px;
    padding: 2px;
    border: 1px solid #2B2B2B;
    color: #AFB1B3;
    height: 100%;
}
</style>

UserName <input type="username" placeholder="UserName" id="github-username-input" oninput="element1=this.parentElement.nextElementSibling.nextElementSibling.nextElementSibling.lastChild.firstChild.firstChild;element2=this.parentElement.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.lastChild.firstChild.firstChild;lines1=element1.innerHTML.split('\n');lines2=element2.innerHTML.split('\n');for(var i=0;i&lt;lines1.length;i++){if(!this.value){v='github-username'}else{v=this.value}if(i===0){lines1[i]=lines1[i].substring(0,153)+v+'&quot;</span>'}};for(var i=0;i&lt;lines2.length;i++){if(!this.value){v='github-username'}else{v=this.value}if(i===0){lines2[i]=lines2[i].substring(0,153)+v+'&quot;</span>'}};element1.innerHTML=lines1.join('\n');element2.innerHTML=lines2.join('\n');">

Email    <input type="email"    placeholder="Email"    id="github-email-input"    oninput="element1=this.parentElement.nextElementSibling.nextElementSibling.lastChild.firstChild.firstChild;element2=this.parentElement.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.lastChild.firstChild.firstChild;lines1=element1.innerHTML.split('\n');lines2=element2.innerHTML.split('\n');for(var i=0;i&lt;lines1.length;i++){if(!this.value){v='github-email'}else{v=this.value}if(i===1){lines1[i]=lines1[i].substring(0,141)+v+'&quot;</span>'}if(i===2){lines1[i]=lines1[i].substring(0,135)+v+'&quot;</span>'}};for(var i=0;i&lt;lines2.length;i++){if(!this.value){v='github-email'}else{v=this.value}if(i===1){lines2[i]=lines2[i].substring(0,141)+v+'&quot;</span>'}if(i===2){lines2[i]=lines2[i].substring(0,208)+v+'&quot;</span>'}};element1.innerHTML=lines1.join('\n');element2.innerHTML=lines2.join('\n');">

### ed25519

```bash
git config --global user.name "github-username"
git config --global user.email "github-email"
ssh-keygen -t ed25519 -C "github-email"


eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

### rsa

```bash
git config --global user.name "github-username"
git config --global user.email "github-email"
ssh-keygen -t rsa -b 4096 -C "github-email"


eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

Скопировать содержимое `*.pub` и вставить в ключи для деплоя в репозиторий

`git clone git@github.com:github-username/github-repo-name.git`
