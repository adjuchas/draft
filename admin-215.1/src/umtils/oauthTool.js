

/*
生成uid函数
 */
import {sha256} from "js-sha256";

function generateUid (){
    let d = new Date().getTime();
    if(window.performance && typeof window.performance.now === "function"){
        d += performance.now(); //use high-precision timer if available
    }
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = (d + Math.random() * 16) % 16 | 0;
        d = Math.floor(d / 16);
        return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16);
    })
}

/**
 *  跳转易班授权服务
 * */

export function sendRedirect(){
    let state=sha256(generateUid());
    window.localStorage.setItem('uid',state)//将uid存储到本地
    window.location.href='https://openapi.yiban.cn/oauth/authorize' +
        '?' + 'client_id=bffa2f6f72f87137' +
        '&redirect_uri=http://120.25.121.177:443/api/oauth/app215' +
        '&state=' + state;
}