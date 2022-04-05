rpc.exports = {
    //加密
    enc: function (data) {
        var res = null
        Java.perform(function () {
            var instance = null
            var key = "9876543210123456"
            var my_enc = Java.use("com.ese.http.encrypt.AesEncryptionBase64")
            instance = my_enc.encrypt(key, data)
            res = instance;
        })

        return res
    },

    //解密
    dec: function (data) {
        var res = null
        Java.perform(function () {
            var instance = null;
            var key = "9876543210123456"
            var my_dec = Java.use("com.ese.http.encrypt.AesEncryptionBase64")
            instance = my_dec.decrypt(key, data)
            res = instance
        })
        return res
    },


}