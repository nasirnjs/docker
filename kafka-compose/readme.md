
**create or overwrite htpasswd file with username admin and password MySecretPass.**\
```bash
echo "admin:$(openssl passwd -apr1 'MySecretPass')" > kafdrop.htpasswd
```

Now log in at `http://host-ip:9000` with:

Username: admin

Password: MySecretPass

[References](https://www.youtube.com/watch?v=BZMgchZp008)

[References](https://github.com/obsidiandynamics/kafdrop)