module.exports = {
    "env": {
        "browser": true,
        "es6": true
    },
    "extends": ["standard","plugin:vue/base"],
    "globals": {
        "Atomics": "readonly",
        "SharedArrayBuffer": "readonly",
        '$': true
    },
    "parserOptions": {
        "ecmaVersion": 2018,
        "sourceType": "module"
    },
    "plugins": [
        "vue"
    ],
    "rules": {
        'prefer-const': 'off'
    }
};