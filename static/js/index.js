function start1(flowNum){
	var result='<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" \
	xmlns:impl="http://impl.webservice.platform.hotent.com/"><soapenv:Header/><soapenv:Body><impl:start> <xml>&lt;';
	result+='req actDefId="" flowKey="gnccspjclfbxlc" subject="" account="010500088803" businessKey="">&lt;data>   &lt;![CDATA[';
    var formDataStr="";
    if(flowNum=="1_1"){
        formDataStr='{"main":{"fields":{"ssdw":"制造本部物流中心","ssdwID":"105040201","ccrID":"10500089559","ccr":"李伟豪",\
        "ygh":"010500089559","zwzc":"其他人员","fygkbm":"制造本部物流中心","fygkbmID":"105040201",\
        "lxfs":"14354653456","ccsy":"1_1 无wbs签认，非包干，无差旅报销单","ccgjksrq":"2017-05-02",\
        "ccgjzzrq":"2017-06-08","ccksdd":"北京","cczzdd":"天津","cczd":"上海","gsfy":"1345","jtgj":"普通列车硬座",\
        "dddw":"中软上海分公司","ccsm":"说明一","xmWBSwlh":"","wbsqrr":"","ckrxm":"王林","zxqh":"1242135465789809",\
        "fj":"1","ndzys":"","sjfse":"","dbxze":"","syed":"","bmshldID":"10500089680","bmshld":"王雪",\
        "bmspldID":"10500017751","bmspld":"胡安祖","fygkbmldID":"10500017751","fygkbmld":"胡安祖",\
        "gsfgspldID":"10500014189","gsfgspld":"田学华","sfczsqsp":"true","bxyccjzqts":"","ccsqjtgjsfcb":"false",\
        "zsfsbsx":"false","ccts":"","cbzsfbzje":"","zsfybxje":"","zsfsjbxje":"","jzfybxje":"","jtfsjbxje":"",\
        "czcfyybxje":"","czcfysjbxje":"","qtfybxje":"","qtfysjbxje":"","btje":"","fyzjdx":"零元","fyzjxx":"0.00",\
        "txcbsx":"","zsfsbsxxk":"","cbzsfbxje":"0","cbzsfsm":"","cbzsfldspjg":"agree","cbjtfbxje":"0",\
        "cbjtfsm":"","cbjtfldspjg":"agree","cbqtfybxje":"0","cbqtfysm":"","cbqtfyldspjg":"agree","xgfj":"",\
        "jtgjdcsc":"单程","sfqrwbs":"false","xcsfbg":"否","sfcywhjk":"是否存有未还借款","sftxccbxd":""}},\
        "sub":[{"tableName":"subtable_gnccspbxbd","fields":[]}],"opinion":[],"bianhao":[]}';
    }else if(flowNum=="1_2"){
        formDataStr='{"main":{"fields":{"ssdw":"制造本部物流中心","ssdwID":"105040201","ccrID":"10500089559","ccr":"李伟豪",\
        "ygh":"010500089559","zwzc":"其他人员","fygkbm":"制造本部物流中心","fygkbmID":"105040201","lxfs":"","ccsy":"1_2 无wbs签认，非包干，有差旅报销单",\
        "ccgjksrq":"2017-05-04","ccgjzzrq":"2017-05-25","ccksdd":"北京","cczzdd":"天津","cczd":"广州","gsfy":"1232",\
        "jtgj":"普通列车硬座","dddw":"中软广州分公司","ccsm":"说明+一","xmWBSwlh":"","wbsqrr":"","ckrxm":"王林",\
        "zxqh":"1242122134321235","fj":"1","ndzys":"","sjfse":"","dbxze":"","syed":"","bmshldID":"10500089680",\
        "bmshld":"王雪","bmspldID":"10500017751","bmspld":"胡安祖","fygkbmldID":"10500017751","fygkbmld":"胡安祖",\
        "gsfgspldID":"10500014189","gsfgspld":"田学华","sfczsqsp":"false","bxyccjzqts":"-21","ccsqjtgjsfcb":"false",\
        "zsfsbsx":"false","ccts":"0","cbzsfbzje":"0.00","zsfybxje":"0.00","zsfsjbxje":"0.00","jzfybxje":"1342.00",\
        "jtfsjbxje":"1342.00","czcfyybxje":"","czcfysjbxje":"","qtfybxje":"","qtfysjbxje":"","btje":"0.00",\
        "fyzjdx":"壹仟叁佰肆拾贰元","fyzjxx":"1342.00","zsfsbsxxk":"","cbzsfbxje":"0","cbzsfsm":"","cbzsfldspjg":"agree",\
        "cbjtfbxje":"0","cbjtfsm":"","cbjtfldspjg":"agree","cbqtfybxje":"0","cbqtfysm":"","cbqtfyldspjg":"agree",\
        "xgfj":"","jtgjdcsc":"单程","sfqrwbs":"false","xcsfbg":"否","sfcywhjk":"是否存有未还借款","sftxccbxd":"true",\
        "txcbsx":""}},"sub":[{"tableName":"subtable_gnccspbxbd","fields":[{"xccfsj":"2017-05-04 16:20:00",\
        "xcddsj":"2017-05-04 19:20:00","xcddd":"广州","xcdddw":"广州中软","xctlqssj":"2017-05-08 16:20:00",\
        "xctlzzsj":"2017-05-25 16:20:00","xcsfpc":"否","xcjtgjlx":"普通列车硬座","xcjtbxfy":"1342","xczsbzfy":"0.00",\
        "xczsbxfy":"","xcbz":"备注一","id":""}]}],"opinion":[],"bianhao":[]}';
     }else if(flowNum=="1_3"){
        formDataStr='{"main":{"fields":{"ssdw":"总部信息技术部","ssdwID":"1050009","ccrID":"10500032580","ccr":"徐娟",\
        "ygh":"010500032580","zwzc":"其他人员","fygkbm":"总部信息技术部","fygkbmID":"1050009","lxfs":"14090872347",\
        "ccsy":"wbs签认，包干，无差旅报销单","ccgjksrq":"2017-05-09","ccgjzzrq":"2017-05-30","ccksdd":"北京",\
        "cczzdd":"天津","cczd":"上海","gsfy":"1421","jtgj":"普通列车硬座","dddw":"中软广州分","ccsm":"工作",\
        "xmWBSwlh":"wbs123","wbsqrr":"","ckrxm":"王林","zxqh":"2313989723458907","fj":"1","ndzys":"","sjfse":"",\
        "dbxze":"","syed":"","bmshldID":"10500032626","bmshld":"张珍文","bmspldID":"10500006053","bmspld":"柳少华",\
        "fygkbmldID":"10500006053","fygkbmld":"柳少华","gsfgspldID":"10000004024569","gsfgspld":"吕任远",\
        "sfczsqsp":"true","bxyccjzqts":"","ccsqjtgjsfcb":"false","zsfsbsx":"false","ccts":"","cbzsfbzje":"",\
        "zsfybxje":"","zsfsjbxje":"","jzfybxje":"","jtfsjbxje":"","czcfyybxje":"","czcfysjbxje":"","qtfybxje":"",\
        "qtfysjbxje":"","btje":"","fyzjdx":"零元","fyzjxx":"0.00","txcbsx":"","zsfsbsxxk":"","cbzsfbxje":"0",\
        "cbzsfsm":"","cbzsfldspjg":"agree","cbjtfbxje":"0","cbjtfsm":"","cbjtfldspjg":"agree","cbqtfybxje":"0",\
        "cbqtfysm":"","cbqtfyldspjg":"agree","xgfj":"","jtgjdcsc":"单程","sfqrwbs":"true","xcsfbg":"是",\
        "sfcywhjk":"是否存有未还借款","sftxccbxd":""}},"sub":[{"tableName":"subtable_gnccspbxbd","fields":[]}],\
        "opinion":[],"bianhao":[]}';
    }else if(flowNum=="1_4"){
        formDataStr='{"main":{"fields":{"ssdw":"制造本部物流中心","ssdwID":"105040201","ccrID":"10500089559","ccr":"李伟豪",\
        "ygh":"010500089559","zwzc":"其他人员","fygkbm":"制造本部物流中心","fygkbmID":"105040201","lxfs":"","ccsy":"1_4 wbs签认，包干，有差旅报销单",\
        "ccgjksrq":"2017-05-04","ccgjzzrq":"2017-05-25","ccksdd":"北京","cczzdd":"天津","cczd":"广州","gsfy":"1232",\
        "jtgj":"普通列车硬座","dddw":"中软广州分公司","ccsm":"说明+一","xmWBSwlh":"1242122","wbsqrr":"","ckrxm":"王林",\
        "zxqh":"1242122134321235","fj":"1","ndzys":"","sjfse":"","dbxze":"","syed":"","bmshldID":"10500089680",\
        "bmshld":"王雪","bmspldID":"10500017751","bmspld":"胡安祖","fygkbmldID":"10500017751","fygkbmld":"胡安祖",\
        "gsfgspldID":"10500014189","gsfgspld":"田学华","sfczsqsp":"false","bxyccjzqts":"-21","ccsqjtgjsfcb":"false",\
        "zsfsbsx":"false","ccts":"0","cbzsfbzje":"0.00","zsfybxje":"0.00","zsfsjbxje":"0.00","jzfybxje":"1342.00",\
        "jtfsjbxje":"1342.00","czcfyybxje":"","czcfysjbxje":"","qtfybxje":"","qtfysjbxje":"","btje":"0.00",\
        "fyzjdx":"壹仟叁佰肆拾贰元","fyzjxx":"1342.00","zsfsbsxxk":"","cbzsfbxje":"0","cbzsfsm":"","cbzsfldspjg":"agree",\
        "cbjtfbxje":"0","cbjtfsm":"","cbjtfldspjg":"agree","cbqtfybxje":"0","cbqtfysm":"","cbqtfyldspjg":"agree",\
        "xgfj":"","jtgjdcsc":"单程","sfqrwbs":"true","xcsfbg":"是","sfcywhjk":"是否存有未还借款","sftxccbxd":"true",\
        "txcbsx":""}},"sub":[{"tableName":"subtable_gnccspbxbd","fields":[{"xccfsj":"2017-05-04 16:20:00",\
        "xcddsj":"2017-05-04 19:20:00","xcddd":"广州","xcdddw":"广州中软","xctlqssj":"2017-05-08 16:20:00",\
        "xctlzzsj":"2017-05-25 16:20:00","xcsfpc":"否","xcjtgjlx":"普通列车硬座","xcjtbxfy":"1342","xczsbzfy":"0.00",\
        "xczsbxfy":"","xcbz":"备注一","id":""}]}],"opinion":[],"bianhao":[]}';
    }
    result+=formDataStr;
    result+=']]&gt;  &lt;/data>   &lt;/req></xml></impl:start></soapenv:Body></soapenv:Envelope>';
	$.ajax({
        type: 'POST',
        headers: {
                    'Content-Type':'text/plain;charset=UTF-8'
                },
        url:'http://122.4.80.27:8081/csrbpm/service/ProcessService',
        data:result,
        success: function(data) {
            var tmp=data.getElementsByTagName("return")[0].childNodes[0].nodeValue;
            if(tmp.indexOf("false")>=0){
                alert('表单验证失败，请检查表单是否正确填写！');
            }else if(tmp.indexOf("run")>=0){
                alert('流程启动成功');

            }else {
            }
        },
        failure : function(response)
        {
            alert('无法连接服务器');
        }
    });
}
function test1(flowNum){
    var url= "http://127.0.0.1:8080/test1/test1?flowNum="+flowNum+"&callback=?";
    $.ajax({
       type: "POST",
       url: url,
       dataType:"jsonp",
       //timeout:300000,
       success:function(data){
            alert('流程测试完成');
            console.log(data.result)
        },
        failure : function(response)
        {
            alert('无法连接服务器');
        }
    })
}