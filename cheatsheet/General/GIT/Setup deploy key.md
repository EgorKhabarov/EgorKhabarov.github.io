# Deploy key

GitHub UserName <input style="border-style: none;display: inline-block;background-color: #191919;min-width: 154px;font-size: 16px;padding: 2px;border: 1px solid #2B2B2B;color: #AFB1B3;height: 100%;" placeholder="UserName" type="username" id="github-username-input" oninput="element=this.parentElement.nextElementSibling.nextElementSibling.lastChild.firstChild.firstChild;lines=element.innerHTML.split('\n');for(var i=0;i&lt;lines.length;i++){if (!this.value){v='github-username'} else {v=this.value};if(i === 0           ){lines[i]=lines[i].substring(0,153)+v+'&quot;</span>';}};element.innerHTML=lines.join('\n')">

Email           <input style="border-style: none;display: inline-block;background-color: #191919;min-width: 154px;font-size: 16px;padding: 2px;border: 1px solid #2B2B2B;color: #AFB1B3;height: 100%;" placeholder="Email"    type="email"    id="github-email-input"    oninput="element=this.parentElement.nextElementSibling                   .lastChild.firstChild.firstChild;lines=element.innerHTML.split('\n');for(var i=0;i&lt;lines.length;i++){if (!this.value){v='github-email'   } else {v=this.value};if(i === 1){lines[i]=lines[i].substring(0,141)+v+'&quot;</span>';};if(i === 2){lines[i]=lines[i].substring(0,135)+v+'&quot;</span>';}};element.innerHTML=lines.join('\n')">


```bash
git config --global user.name "github-username"
git config --global user.email "github-email"
ssh-keygen -t ed25519 -C "github-email"


eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

`ssh-keygen -t rsa -b 4096 -C "github-email"`

Скопировать содержимое `id_rsa.pub` и вставить в ключи для деплоя в репозиторий

`git clone git@github.com:github-username/github-repo-name.git`
