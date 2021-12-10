path "secret/*" {
    capabilities = ["read", "update", "list"]
}

path "secret/admin" {
    capabilities = ["deny"]
}

path "sys/mounts" {
    capabilities = [ "read" ]
}

path "sys/auth" {
    capabilities = [ "read" ]
}
