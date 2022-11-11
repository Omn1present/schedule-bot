var prev_val_e = -1;
var nocomfirm=false;
var warnCounter;
var centerHint = false
var MsgEmpyError = 'Не все поля заполнены!'

function first_field_ias()
    {
      document.forms(0).p_filter2.focus();
      return;
    }
function getName(obj){
  return (obj.name)?obj.name:obj.id
}
function getObject(name){	
  var obj
  if (document.all)
    obj=document.all[name]
  else
  {
    obj=document.getElementById(name)
    if (!obj)
      obj=document.getElementsByName(name)[0]
    if (document.getElementsByName(name).length>1)
      obj=document.getElementsByName(name)
  }
  return obj
}
function showHint(link, show){
	var num = getName(link)
        var obj = getObject("hint_" + num)
        if (obj) {obj.style.visibility = show?"visible":"hidden"}
}
function corrHint(link, x, y){
	var num = getName(link)
	var hnt = getObject("hint_" + num)
	if (hnt) {
          hnt.style.left = x + document.body.scrollLeft - (centerHint?70:2)
	  hnt.style.top = y + document.body.scrollTop + 16
        }
}
var isGecko = navigator.appName == "Netscape"
var isOpera = navigator.userAgent.indexOf("Opera") > -1
function mOver(e){
	if (isOpera) corrHint(event.srcElement, event.clientX, event.clientY)
	if (isGecko) showHint(e.target, true)
	else showHint(event.srcElement, true)
}
function mOut(e){
	if (isGecko) showHint(e.target, false)
	else showHint(event.srcElement, false)
}
function mMove(e){
	if (isGecko) corrHint(e.target, e.pageX, e.pageY)
	else corrHint(event.srcElement, event.clientX, event.clientY)
}

  /*PopUp Functionality*/

function ias_PopUp(pURL,pName,pWidth,pHeight,pTop,pLeft,PropWindow){
  if(!pURL){pURL = 'about:blank'}
  if(!pName){pName = 'Popup'}
  if(!pWidth){pWidth = screen.availwidth-10}
  if(!pHeight){pHeight = screen.availheight-1}
  if(!pTop){pTop = 0}
  if(pTop==-1){pTop = (screen.availheight-pHeight)/2}
  if(!pLeft){pLeft = 0}
  if(pLeft==-1){pLeft = (screen.availwidth-pWidth)/2}
  if(!PropWindow) {PropWindow = 'toolbar=0,scrollbars=1,location=0,statusbar=0,menubar=0,resizable=1,'}
  l_Window = window.open(pURL,pName, 
    PropWindow+'width='+pWidth+',height='+pHeight+',left='+pLeft+',top='+pTop);
  if (l_Window.opener == null){l_Window.opener = self;}
  l_Window.focus();
//  return l_Window;
}

function OnLoadPageLoadFile(p_item_name,p_value)
{
     if (p_value) {
        if (opener.document.getElementById(p_item_name))
        {
          opener.document.getElementById(p_item_name).value = p_value;
        }
        window.close();
     }
}

function GetWindowName(url) {
  minus = '-';
  dot = '.';
  while (url.indexOf(minus) != -1) {
    url = url.replace(minus);
  }
  while (url.indexOf(dot) != -1) {
    url = url.replace(dot);
  }

  return url;
}

function IAS_GET_AJAX_TEXT(url) {
   html_processing();
   var p;
   try {
      p = new XMLHttpRequest();
    } catch (e) {
      p = new ActiveXObject("Msxml2.XMLHTTP");
//      p = new ActiveXObject("Msxml2.XMLHTTP.4.0");
    }
    try {
        p.open("GET", url, false);
    	p.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
        p.send(null);
        setTimeout(html_Doneprocessing,1);
        return p.responseText;
    } catch (e) {
       setTimeout(html_Doneprocessing,1);
       alert('Error AJAX!')
       return;
    }
  return;
}

function IAS_GET_AJAX_XML(url) {
	   html_processing();
	   var p;
	   try {
	      p = new XMLHttpRequest();
	    } catch (e) {
	      p = new ActiveXObject("Msxml2.XMLHTTP");
//	      p = new ActiveXObject("Msxml2.XMLHTTP.4.0");
	    }
	    try {
	        p.open("GET", url, false);
	    	p.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
	        p.send(null);
	        setTimeout(html_Doneprocessing,1);
	        return p.responseXML;
	    } catch (e) {
	       setTimeout(html_Doneprocessing,1);
	       alert('Error AJAX!')
	       return;
	    }
	  return;
	}

function IAS_Change_Context_AJAX(elem, newsrc){
  elem.innerHTML=newsrc;
  return;
}

function IAS_NEW_AJAX_SRC(url, divname) {
  celem = document.getElementById(divname);
  newsrc = IAS_GET_AJAX_TEXT(url);
  IAS_Change_Context_AJAX(celem,newsrc);
  return;
}

function IAS_Change_Groups(newfac){
  celem = document.getElementById('GROUPS_AJAX');
  newsrc = IAS_GET_AJAX_TEXT('WEB_IAS_TT_AJX_GROUPS?p_id_fac='+newfac);
  IAS_Change_Context_AJAX(celem,newsrc);
  return;
}

//load xslt
function load_xslt(){
  xsldoc = IAS_GET_AJAX_XML('/i/ias/css/xml_tt_group_formater2.xsl');
}

function IAS_Change_Groups2(newfac){
	  celem = document.getElementById('GROUPS_AJAX');

	  ts = document.getElementsByName("tabs");
	  for ( i = 0; i < ts.length; i++ ) {
		  ts[i].setAttribute("class", "");
	  }
  
	  document.getElementById(newfac).setAttribute("class", "tabcurrent");
	  
	  var newsrc = IAS_GET_AJAX_XML('WEB_IAS_TT_AJX_GROUPS2?p_id_fac='+newfac);
	  
	  
   var proc = new XSLTProcessor();
      proc.importStylesheet(xsldoc);
      var xhtmldoc = proc.transformToDocument(newsrc);
      var ser = new XMLSerializer();
      newsrc=ser.serializeToString(xhtmldoc);
	  
	  IAS_Change_Context_AJAX(celem,newsrc);
	  
	  return;
	}

function IAS_Change_Potoks(newfac){
  celem = document.getElementById('POTOKS_AJAX');
  newsrc = IAS_GET_AJAX_TEXT('WEB_IAS_TT_AJX_POTOKS?p_id_fac='+newfac);
  IAS_Change_Context_AJAX(celem,newsrc);
  return;
}

function IAS_Change_Kaf(newfac, newKaf){
  celem = document.getElementById('TEACHS_AJAX');
  newsrc = IAS_GET_AJAX_TEXT('WEB_IAS_TT_AJX_TEACHS?p_id_fac='+newfac+'&p_id_kaf='+newKaf);
  IAS_Change_Context_AJAX(celem,newsrc);
  return;
}

function IAS_Change_Teach_Kaf(newfac, newKaf){
  celem = document.getElementById('TEACHS_AJAX');
  newsrc = IAS_GET_AJAX_TEXT('WEB_IAS_TT_AJX_TEACHS_KAF?p_id_fac='+newfac+'&p_id_kaf='+newKaf);
  IAS_Change_Context_AJAX(celem,newsrc);
  return;
}

function IAS_Teach_Find(surname){
  celem = document.getElementById('TEACHS_AJAX');
  newsrc = IAS_GET_AJAX_TEXT('WEB_IAS_TT_AJX_TEACHS_FIND?p_surname='+surname);
  IAS_Change_Context_AJAX(celem,newsrc);
  return;
}

function IAS_Group_Find(surname){
  celem = document.getElementById('GROUPS_AJAX');
  newsrc = IAS_GET_AJAX_TEXT('WEB_IAS_TT_AJX_GROUPS_FIND?p_group='+surname);
  IAS_Change_Context_AJAX(celem,newsrc);
  return;
}

function IAS_ADD_Group_in_List(naimgroup, idgroup){
  elem = document.getElementById('CHOISE_GROUPS');
  melem = (ie) ? elem.all : elem.getElementsByTagName('*'); 
  var fl=0;
  for ( i = 0; i < melem.length; i++ ) {
   if (melem[i].id==idgroup) {
    fl=1;
    break;
   }
  }
  if (!fl) {

      oldHTML = elem.innerHTML;
      newHTML = oldHTML+'<div name="'+idgroup+'" id="'+idgroup+'">&nbsp&nbsp&nbsp&nbsp<a href="#" onClick="javascript:IAS_DEL_Group_from_List('+"'"+idgroup+"'"+')";>'+naimgroup+'</a><br></div>';
      elem.innerHTML = newHTML;
  }
}


function IAS_ADD_Potok_in_List(naimpotok, idgroups){
  celem = document.getElementById('CHOISE_POTOKS');
  oldHTML = celem.innerHTML;
  newHTML = '<div name="'+idgroups+'" id="'+idgroups+'">&nbsp&nbsp&nbsp&nbsp<a href="#" onClick="javascript:IAS_DEL_Group_from_List('+"'"+idgroups+"'"+')";>'+naimpotok+'</a><br></div>';
  celem.innerHTML = newHTML;
  return;
}

function IAS_ADD_Teach_in_List(naimteach, idteach){
  elem = document.getElementById('CHOISE_TEACHS');
  melem = (ie) ? elem.all : elem.getElementsByTagName('*'); 
  var fl=0;
  for ( i = 0; i < melem.length; i++ ) {
   if (melem[i].id==idteach) {
    fl=1;
    break;
   }
  }
  if (!fl) {
      oldHTML = elem.innerHTML;
      newHTML = oldHTML+'<div name="'+idteach+'" id="'+idteach+'">&nbsp&nbsp&nbsp&nbsp<a href="#" onClick="javascript:IAS_DEL_Group_from_List('+"'"+idteach+"'"+')";>'+naimteach+'</a><br></div>';
      elem.innerHTML = newHTML;
  }
  return;
}


function IAS_ADD_Aud_in_List(naimaud, idaud){
  elem = document.getElementById('CHOISE_AUDS');
  melem = (ie) ? elem.all : elem.getElementsByTagName('*');
  var fl=0;
  for ( i = 0; i < melem.length; i++ ) {
   if (melem[i].id==idaud) {
    fl=1;
    break;
   }
  }
  if (!fl) {
      oldHTML = elem.innerHTML;
      newHTML = oldHTML+'<div name="'+idaud+'" id="'+idaud+'">&nbsp&nbsp&nbsp&nbsp<a href="#" onClick="javascript:IAS_DEL_Group_from_List('+"'"+idaud+"'"+')";>'+naimaud+'</a><br></div>';
      elem.innerHTML = newHTML;
  }
  return;
}

function IAS_DEL_Group_from_List(delelemid){
  if (ie || isOpera) {
    elem = document.getElementById(delelemid);  
    elem.outerHTML = '';
  } else {
    elem = document.getElementById(delelemid);
    parent = elem.parentNode;
    parent.removeChild(elem);
  }
  return;
}


function IAS_GET_STR_ID(choise_reg){
  elem = document.getElementById(choise_reg);
  melem = (ie) ? elem.all : elem.getElementsByTagName('*'); 

  var Str='';
  for ( i = 0; i < melem.length; i++ ) {
   if (melem[i].id!='') {
     if (i!=0) {Str = Str+'_';}
     Str = Str+melem[i].id; 
   }
  }
  return Str;
}

function IAS_GET_STR_CHECKBOX_VALUES(choise_reg){
  var Str ='';
  var Counter = 0;
  elem = document.getElementById(choise_reg);
  melem = (ie) ? elem.all : elem.getElementsByTagName('*'); 
  for ( i = 0; i < melem.length; i++ ) {
    if (melem[i].type == 'checkbox') {
      if (Counter!=0) {
        if (melem[i].checked) {Str = Str+'_';}
      }
      if (melem[i].checked) { 
      Str = Str+melem[i].value;
      Counter = Counter + 1;
      }
    }
  }
  return Str;
}

function IAS_GET_RADIO_VALUES(choise_reg){
  var Str ='';
  elem = document.getElementById(choise_reg);
  melem = (ie) ? elem.all : elem.getElementsByTagName('*'); 
  for ( i = 0; i < melem.length; i++ ) {
    if (melem[i].type == 'radio') {
      if (melem[i].checked) { 
      Str = melem[i].value;
      }
    }
  }
  return Str;
}

function IAS_GET_FIRST_DATE(apage_number) {
  dt_type = IAS_GET_RADIO_VALUES('CHOISE_DATE_TYPE');
  var CurPage = document.getElementById('pFlowStepId').value;         
  if (dt_type == 'DT_DATE') {
    return document.getElementById('P'+CurPage+'_DATE_BEGIN').value;
  }
  else if (dt_type == 'DT_WEEK') {
    return document.getElementById('P'+CurPage+'_WEEK_BEGIN').value;
  } 
  else if (dt_type == 'DT_DAY') {
    return document.getElementById('P'+CurPage+'_CURRENT_DAY').value;
  }
  else if (dt_type == 'DT_CURR_DAY') {
    return document.getElementById('P'+CurPage+'_RASP_DATE').value;
  }
  else if (dt_type == 'DT_TOMORROW') {
    return document.getElementById('P'+CurPage+'_TOMORROW_DAY').value;
  }  
  else if (dt_type == 'DT_NEXTWEEK') {
    return document.getElementById('P'+CurPage+'_NEXTWEEK_BEGIN').value;
  }    
}


function IAS_GET_LAST_DATE(apage_number) {
  dt_type = IAS_GET_RADIO_VALUES('CHOISE_DATE_TYPE');
  var CurPage = document.getElementById('pFlowStepId').value;
  if (dt_type == 'DT_DATE') {
    return document.getElementById('P'+CurPage+'_DATEEND').value;
  }
  else if (dt_type == 'DT_WEEK') {
    return document.getElementById('P'+CurPage+'_WEEK_END').value;
  } 
  else if (dt_type == 'DT_DAY') {
    return document.getElementById('P'+CurPage+'_CURRENT_DAY').value;
  }
  else if (dt_type == 'DT_CURR_DAY') {
    return document.getElementById('P'+CurPage+'_RASP_DATE').value;
  }
  else if (dt_type == 'DT_TOMORROW') {
    return document.getElementById('P'+CurPage+'_TOMORROW_DAY').value;
  }  
  else if (dt_type == 'DT_NEXTWEEK') {
    return document.getElementById('P'+CurPage+'_NEXTWEEK_END').value;
  }      
}


 /* IAS_TT_HTML */
function IAS_GROUP_TT_HTML(session) {
  group = IAS_GET_STR_ID('CHOISE_GROUPS');
  firstdate = IAS_GET_FIRST_DATE(2);
  lastdate  = IAS_GET_LAST_DATE(2);
  //alert(firstdate+'##'+lastdate);
  if (session && firstdate && lastdate && group){
    url = "f?p=778:201:" +session+ ":::201:P201_FIRST_DATE,P201_LAST_DATE,P201_GROUP,P201_POTOK:"+ firstdate+ "," +lastdate+ "," +group+ ",0:";
    ias_PopUp(url, group,800,600,-1,-1);
  } 
  else {
    alert(MsgEmpyError);
  }
}

function IAS_GROUP_FIND_TT_HTML(session) {
  group = IAS_GET_STR_ID('CHOISE_GROUPS');
  firstdate = IAS_GET_FIRST_DATE(12);
  lastdate  = IAS_GET_LAST_DATE(12);
  if (session && firstdate && lastdate && group){
    url = "f?p=778:201:" +session+ ":::201:P201_FIRST_DATE,P201_LAST_DATE,P201_GROUP,P201_POTOK:"+ firstdate+ "," +lastdate+ "," +group+ ",0:";
    ias_PopUp(url, group,800,600,-1,-1);
  } 
  else {
    alert(MsgEmpyError);
  }
}


function IAS_TEACH_TT_HTML(session) {
  teach = IAS_GET_STR_ID('CHOISE_TEACHS');
  firstdate = IAS_GET_FIRST_DATE(4);
  lastdate  = IAS_GET_LAST_DATE(4);

  if (session && firstdate && lastdate && teach){
    url = "f?p=778:202:" +session+ ":::202:P202_FIRST_DATE,P202_LAST_DATE,P202_SOTR,P202_KAF:"+ firstdate+ "," +lastdate+ "," +teach+ ",0:";
    ias_PopUp(url, teach,800,600,-1,-1);
  } 
  else {
    alert(MsgEmpyError);
  }
}

function IAS_TEACH_FIND_TT_HTML(session) {
  teach = IAS_GET_STR_ID('CHOISE_TEACHS');
  firstdate = IAS_GET_FIRST_DATE(11);
  lastdate  = IAS_GET_LAST_DATE(11);

  if (session && firstdate && lastdate && teach){
    url = "f?p=778:202:" +session+ ":::202:P202_FIRST_DATE,P202_LAST_DATE,P202_SOTR,P202_KAF:"+ firstdate+ "," +lastdate+ "," +teach+ ",0:";
    ias_PopUp(url, teach,800,600,-1,-1);
  } 
  else {
    alert(MsgEmpyError);
  }
}

function IAS_TEACH_KAF_TT_HTML(session) {
  kaf = document.getElementById('p_id_kaf').value;
  firstdate = IAS_GET_FIRST_DATE(5);
  lastdate  = IAS_GET_LAST_DATE(5);
  if (session && firstdate && lastdate && kaf){
    npage = "202";
    itemsnames  = "\\P202_FIRST_DATE,P202_LAST_DATE,P202_SOTR,P202_KAF\\";
    itemsvalues = "\\"+firstdate+ "," +lastdate+ ",,"+kaf+"\\";
    urlwaitpg = "f?p=778:200:" +session+ ":::200:P200_NPAGE,P200_ITEMSNAMES,P200_ITEMSVALUES:"+npage+","+itemsnames+","+itemsvalues+":";
    ias_PopUp(urlwaitpg, kaf,800,600,-1,-1);
  } 
  else {
    alert(MsgEmpyError);
  }
}

function IAS_POTOK_TT_HTML(session) {
  elem = document.getElementById('CHOISE_POTOKS');
  try{
    var Str = (ie) ? elem.all.item(0).id : elem.getElementsByTagName('*')[0].id;  
  }
  catch (e) {             
    var Str = '';
  }
  firstdate = IAS_GET_FIRST_DATE(3);
  lastdate  = IAS_GET_LAST_DATE(3);
  if (session && firstdate && lastdate && Str){
    url = "f?p=778:201:" +session+ ":::201:P201_FIRST_DATE,P201_LAST_DATE,P201_GROUP,P201_POTOK:"+ firstdate+ "," +lastdate+ "," +Str+ ",0:";
    ias_PopUp(url, Str,800,600,-1,-1);
  } 
  else {
    alert(MsgEmpyError);
  }
}

function IAS_AUD_TT_HTML(session) {
  aud = IAS_GET_STR_ID('CHOISE_AUDS');
  firstdate = IAS_GET_FIRST_DATE(6);
  lastdate  = IAS_GET_LAST_DATE(6);
  if (session && firstdate && lastdate && aud){
    url = "f?p=778:203:" +session+ ":::203:P203_FIRST_DATE,P203_LAST_DATE,P203_AUD:"+ firstdate+ "," +lastdate+ "," +aud;
    ias_PopUp(url, GetWindowName(aud),800,600,-1,-1);
  } 
  else {
    alert(MsgEmpyError);
  }
}


function IAS_AUD_ONE_DAY_TT_HTML(session) {
  pairs = IAS_GET_STR_CHECKBOX_VALUES('CHOISE_PAIRS');
  firstdate = IAS_GET_FIRST_DATE(7);
  lastdate  = IAS_GET_LAST_DATE(7);
  raspdate = document.getElementById('P7_RASP_DATE').value;
  if (session && firstdate && lastdate && pairs && raspdate){
    url = "f?p=778:204:" +session+ ":::204:P204_FIRST_DATE,P204_LAST_DATE,P204_RASP_DATE,P204_PAIRS:" + firstdate + "," + lastdate + "," + raspdate + "," + pairs;
    ias_PopUp(url, GetWindowName(raspdate),800,600,-1,-1);
  } 
  else {
    alert(MsgEmpyError);
  }
}


function IAS_AUD_ONE_DAY_BUSY_HTML(session) {
  pairs = IAS_GET_RADIO_VALUES('CHOISE_PAIRS');
  firstdate = IAS_GET_FIRST_DATE(8);
  lastdate  = IAS_GET_LAST_DATE(8);
  raspdate = document.getElementById('P8_RASP_DATE').value;
  if (session && firstdate && lastdate && pairs && raspdate){
    url = "f?p=778:205:" +session+ ":::205:P205_FIRST_DATE,P205_LAST_DATE,P205_RASP_DATE,P205_PAIRS:" + firstdate + "," + lastdate + "," + raspdate + "," + pairs;
    ias_PopUp(url, GetWindowName(raspdate.concat(pairs)),800,600,-1,-1);
  } 
  else {
    alert(MsgEmpyError);
  }
}

//Chen
function IAS_KORP_BUSY_HTML(session) {
  //pairs = IAS_GET_RADIO_VALUES('CHOISE_PAIRS');
  //firstdate = IAS_GET_FIRST_DATE(8);
  //lastdate  = IAS_GET_LAST_DATE(8);
  //raspdate = document.getElementById('P8_RASP_DATE').value;
  if (session){
    url = "f?p=778:502:"+session+":";
	ias_PopUp(url,'123',610,420,-1,-1);
	} 
  else {
    alert(MsgEmpyError);
	
  }
}

 /* IAS_TT_EXCEL */

function IAS_GROUP_TT_EXCEL(session) {
  var url;
  group = IAS_GET_STR_ID('CHOISE_GROUPS');
  firstdate = IAS_GET_FIRST_DATE(2);
  lastdate  = IAS_GET_LAST_DATE(2);
  
   
  if (session && firstdate && lastdate && group){
    url ="WEB_IAS_TT_GNR_RASP.GEN_GROUP_POTOK_RASP?ATypeDoc=2&Aid_group=" + group + "&Aid_potok=0&ADateStart=" + firstdate + "&ADateEnd=" + lastdate + "&AMultiWorkSheet=";
    if (document.getElementById('P2_MULTI_PAGE').checked) {
      url = url + 1;
    }
    else
    {
      url = url + 0;
    }
    window.location = url;
  } 
  else {
    alert(MsgEmpyError);
  }
}

function IAS_GROUP_FIND_TT_EXCEL(session) {
  var url;
  group = IAS_GET_STR_ID('CHOISE_GROUPS');
  firstdate = IAS_GET_FIRST_DATE(12);
  lastdate  = IAS_GET_LAST_DATE(12);
  if (session && firstdate && lastdate && group){
    url ="WEB_IAS_TT_GNR_RASP.GEN_GROUP_POTOK_RASP?ATypeDoc=2&Aid_group=" + group + "&Aid_potok=0&ADateStart=" + firstdate + "&ADateEnd=" + lastdate + "&AMultiWorkSheet=";
    if (document.getElementById('P12_MULTI_PAGE').checked) {
      url = url + 1;
    }
    else
    {
      url = url + 0;
    }
    window.location = url;
  } 
  else {
    alert(MsgEmpyError);
  }
}

function IAS_TEACH_TT_EXCEL(session) {
  var url;
  teach = IAS_GET_STR_ID('CHOISE_TEACHS');
  firstdate = IAS_GET_FIRST_DATE(4);
  lastdate  = IAS_GET_LAST_DATE(4);
  if (session && firstdate && lastdate && teach){
    url ="WEB_IAS_TT_GNR_RASP.GEN_TEACHER_KAF_RASP?ATypeDoc=2&Aid_sotr=" +teach+ "&Aid_kaf=0&ADateStart=" + firstdate + "&ADateEnd=" + lastdate + "&AMultiWorkSheet=";
    if (document.getElementById('P4_MULTI_PAGE').checked) {
      url = url + 1;
    }
    else
    {
      url = url + 0;
    }
    window.location = url;
  } 
  else {
    alert(MsgEmpyError);
  }
}


function IAS_TEACH_FIND_TT_EXCEL(session) {
  var url;
  teach = IAS_GET_STR_ID('CHOISE_TEACHS');
  firstdate = IAS_GET_FIRST_DATE(11);
  lastdate  = IAS_GET_LAST_DATE(11);
  if (session && firstdate && lastdate && teach){
    url ="WEB_IAS_TT_GNR_RASP.GEN_TEACHER_KAF_RASP?ATypeDoc=2&Aid_sotr=" +teach+ "&Aid_kaf=0&ADateStart=" + firstdate + "&ADateEnd=" + lastdate + "&AMultiWorkSheet=";
    if (document.getElementById('P11_MULTI_PAGE').checked) {
      url = url + 1;
    }
    else
    {
      url = url + 0;
    }
    window.location = url;
  } 
  else {
    alert(MsgEmpyError);
  }
}


function IAS_TEACH_KAF_TT_EXCEL(session) {
  kaf = document.getElementById('p_id_kaf').value;
  firstdate = IAS_GET_FIRST_DATE(5);
  lastdate  = IAS_GET_LAST_DATE(5);
  if (session && firstdate && lastdate && kaf){
    url ="WEB_IAS_TT_GNR_RASP.GEN_TEACHER_KAF_RASP?ATypeDoc=2&Aid_sotr=&Aid_kaf="+kaf+"&ADateStart=" + firstdate + "&ADateEnd=" + lastdate + "&AMultiWorkSheet=";
    if (document.getElementById('P5_MULTI_PAGE').checked) {
      url = url + 1;
    }
    else
    {
      url = url + 0;
    }
    window.location = url;
  } 
  else {
    alert(MsgEmpyError);
  }
}

function IAS_POTOK_TT_EXCEL(session) {
  elem = document.getElementById('CHOISE_POTOKS');
  try{
    var Str = (ie) ? elem.all.item(0).id : elem.getElementsByTagName('*')[0].id;  
  }
  catch (e) {             
    var Str = '';
  }
  firstdate = IAS_GET_FIRST_DATE(3);
  lastdate  = IAS_GET_LAST_DATE(3);
  if (session && firstdate && lastdate && Str){
    url ="WEB_IAS_TT_GNR_RASP.GEN_GROUP_POTOK_RASP?ATypeDoc=2&Aid_group=" + Str + "&Aid_potok=0&ADateStart=" + firstdate + "&ADateEnd=" + lastdate + "&AMultiWorkSheet=";
    if (document.getElementById('P3_MULTI_PAGE').checked) {
      url = url + 1;
    }
    else
    {
      url = url + 0;
    }
    window.location = url;
  } 
  else {
    alert(MsgEmpyError);
  }
}

function IAS_AUD_TT_EXCEL(session) {
  var url;
  aud = IAS_GET_STR_ID('CHOISE_AUDS');
  firstdate = IAS_GET_FIRST_DATE(6);
  lastdate  = IAS_GET_LAST_DATE(6);
  if (session && firstdate && lastdate && aud){
    url ="WEB_IAS_TT_GNR_RASP.GEN_AUD_RASP?ATypeDoc=2&Aid_aud=" + aud + "&ADateStart=" + firstdate + "&ADateEnd=" + lastdate + "&AMultiWorkSheet=";
    if (document.getElementById('P6_MULTI_PAGE').checked) {
      url = url + 1;
    }
    else
    {
      url = url + 0;
    }
    window.location = url;
  } 
  else {
    alert(MsgEmpyError);
  }
}


 /* IAS_TT_OUTLOOK */


function IAS_TEACH_TT_OUTLOOK(session) {
  var url;
  teach = IAS_GET_STR_ID('CHOISE_TEACHS');
  firstdate = IAS_GET_FIRST_DATE(4);
  lastdate  = IAS_GET_LAST_DATE(4);
  if (session && firstdate && lastdate && teach){
    url ="WEB_IAS_TT_GNR_RASP.GEN_TEACHER_KAF_RASP?ATypeDoc=3&Aid_sotr=" +teach+ "&Aid_kaf=0&ADateStart=" + firstdate + "&ADateEnd=" + lastdate + "&AMultiWorkSheet=0";
    window.location = url;
  } 
  else {
    alert(MsgEmpyError);
  }
}


function IAS_TEACH_FIND_TT_OUTLOOK(session) {
  var url;
  teach = IAS_GET_STR_ID('CHOISE_TEACHS');
  firstdate = IAS_GET_FIRST_DATE(11);
  lastdate  = IAS_GET_LAST_DATE(11);
  if (session && firstdate && lastdate && teach){
    url ="WEB_IAS_TT_GNR_RASP.GEN_TEACHER_KAF_RASP?ATypeDoc=3&Aid_sotr=" +teach+ "&Aid_kaf=0&ADateStart=" + firstdate + "&ADateEnd=" + lastdate + "&AMultiWorkSheet=0";
    window.location = url;
  } 
  else {
    alert(MsgEmpyError);
  }
}


function IAS_AUD_TT_OUTLOOK(session) {
  var url;
  aud = IAS_GET_STR_ID('CHOISE_AUDS');
  firstdate = IAS_GET_FIRST_DATE(6);
  lastdate  = IAS_GET_LAST_DATE(6);
  if (session && firstdate && lastdate && aud){
    url ="WEB_IAS_TT_GNR_RASP.GEN_AUD_RASP?ATypeDoc=3&Aid_aud=" + aud + "&ADateStart=" + firstdate + "&ADateEnd=" + lastdate + "&AMultiWorkSheet=0";
    window.location = url;
  } 
  else {
    alert(MsgEmpyError);
  }
}

function IAS_POTOK_TT_OUTLOOK(session) {
  elem = document.getElementById('CHOISE_POTOKS');
  try{
    var Str = (ie) ? elem.all.item(0).id : elem.getElementsByTagName('*')[0].id;  
  }
  catch (e) {             
    var Str = '';
  }
  firstdate = IAS_GET_FIRST_DATE(3);
  lastdate  = IAS_GET_LAST_DATE(3);
  if (session && firstdate && lastdate && Str){
    url ="WEB_IAS_TT_GNR_RASP.GEN_GROUP_POTOK_RASP?ATypeDoc=3&Aid_group=" + Str + "&Aid_potok=0&ADateStart=" + firstdate + "&ADateEnd=" + lastdate + "&AMultiWorkSheet=0";
    window.location = url;
  } 
  else {
    alert(MsgEmpyError);
  }
}

function IAS_TEACH_KAF_TT_OUTLOOK(session) {
  kaf = document.getElementById('p_id_kaf').value;
  firstdate = IAS_GET_FIRST_DATE(5);
  lastdate  = IAS_GET_LAST_DATE(5);
  if (session && firstdate && lastdate && kaf){
    url ="WEB_IAS_TT_GNR_RASP.GEN_TEACHER_KAF_RASP?ATypeDoc=3&Aid_sotr=&Aid_kaf="+kaf+"&ADateStart=" + firstdate + "&ADateEnd=" + lastdate + "&AMultiWorkSheet=0";
    window.location = url;
  } 
  else {
    alert(MsgEmpyError);
  }
}


function IAS_GROUP_TT_OUTLOOK(session) {
  var url;
  group = IAS_GET_STR_ID('CHOISE_GROUPS');
  firstdate = IAS_GET_FIRST_DATE(2);
  lastdate  = IAS_GET_LAST_DATE(2);
  if (session && firstdate && lastdate && group){
    url ="WEB_IAS_TT_GNR_RASP.GEN_GROUP_POTOK_RASP?ATypeDoc=3&Aid_group=" + group + "&Aid_potok=0&ADateStart=" + firstdate + "&ADateEnd=" + lastdate + "&AMultiWorkSheet=0";
    window.location = url;
  } 
  else {
    alert(MsgEmpyError);
  }
}

function IAS_GROUP_FIND_TT_OUTLOOK(session) {
  var url;
  group = IAS_GET_STR_ID('CHOISE_GROUPS');
  firstdate = IAS_GET_FIRST_DATE(12);
  lastdate  = IAS_GET_LAST_DATE(12);
  if (session && firstdate && lastdate && group){
    url ="WEB_IAS_TT_GNR_RASP.GEN_GROUP_POTOK_RASP?ATypeDoc=3&Aid_group=" + group + "&Aid_potok=0&ADateStart=" + firstdate + "&ADateEnd=" + lastdate + "&AMultiWorkSheet=0";
    window.location = url;
  } 
  else {
    alert(MsgEmpyError);
  }
}



//____________________Chen___________________________________________________________________________________


//AJAX Rang departmens 
function IAS_RANG_KAF(new_id, year){
  var celem = document.getElementById('RANG_KAF');
  var newsrc = IAS_GET_AJAX_TEXT('WEB_IAS_RANG_KAF?p_Item='+new_id+'&p_year='+year);
  IAS_Change_Context_AJAX(celem,newsrc);
  return;
}



//Calculating result & changing styles
function IAS_CALC_STUD_ACTIVITIES(ip_stud, ip_fio) { 
  var temp_value = document.getElementById(ip_stud).value;
  var elem1;
  var elem2;
  var SumP = 0;
  var SumZ = 0;
  
  //alert('temp_value: !'+temp_value+'! ');
  
  document.getElementById(ip_stud).style.borderColor = '#2F4F4F';
  document.getElementById(ip_stud).style.backgroundColor = 	'#FFFFFF';
  document.getElementById('ad'+ip_stud.substring(2,100)).style.borderColor = '#2F4F4F';
  document.getElementById('ad'+ip_stud.substring(2,100)).style.backgroundColor = '#BEBEBE';
 
  if (ip_stud.substring(1,2) == "p" ) {
	elem1 = document.getElementById(ip_stud);
	elem2 = document.getElementById(ip_stud.replace('p','z'));
   }else{
	elem2 = document.getElementById(ip_stud);
	elem1 = document.getElementById(ip_stud.replace('z','p'));
   }
  
  if (parseInt(elem1.value,10)<parseInt(elem2.value,10)) {
	elem1.style.borderColor = '#FF3030';
	elem1.style.backgroundColor = '#EE9572';
	elem2.style.borderColor = elem1.style.borderColor;
	elem2.style.backgroundColor = elem1.style.backgroundColor;
	} else {
	elem1.style.borderColor = '#2F4F4F';
	elem1.style.backgroundColor = '#FFFFFF'; // '#B0C4DE' ;
	elem2.style.borderColor = elem1.style.borderColor;;
	elem2.style.backgroundColor = elem1.style.backgroundColor;
	}

	for(var i=1; i<5; i++){
	 SumP = SumP + parseInt(document.getElementById(i+'p'+ip_stud.substring(2,100)).value,10);
	 SumZ = SumZ + parseInt(document.getElementById(i+'z'+ip_stud.substring(2,100)).value,10);
	}
	
	document.getElementById('ap'+ip_stud.substring(2,100)).value = SumP;
	document.getElementById('az'+ip_stud.substring(2,100)).value = SumZ;
	document.getElementById('ad'+ip_stud.substring(2,100)).value = SumP - SumZ;	
	
	if((SumP - SumZ) < 0) {
	document.getElementById('ad'+ip_stud.substring(2,100)).style.borderColor = '#FF3030';
	document.getElementById('ad'+ip_stud.substring(2,100)).style.backgroundColor = '#EE9572';
	
	}
}

function IAS_CHECK_LOAD(path){
	//alert(path);
    url = path+document.getElementById("P800_TYPE_CALC_DISC").value;
    //alert(url);
	ias_PopUp(url,'',800,600,250,350);
}
//journal
var mas_style = null;
var tr_obj = null;
var tr_mas = null;
var mas_tr_obj = [];
var mas_tr_tag = [];
function show_img() { document.getElementById("load_img").style.display = "inline"; }
function hide_img() { document.getElementById("load_img").style.display = "none"; }


function getStyleVal(el, cssprop) {
    if (document.defaultView && document.defaultView.getComputedStyle) {//Normal
        if (cssprop == 'float') cssprop = 'cssFloat';
        st_obj = document.defaultView.getComputedStyle(el, '');

        var srt_n_s = cssprop;
        var i_f = srt_n_s.search('-');
        while (i_f != -1) {
            srt_n_s = srt_n_s.substring(0, i_f).toLowerCase() + srt_n_s.charAt(i_f + 1).toUpperCase() + srt_n_s.substr(i_f + 2).toLowerCase();
            i_f = srt_n_s.search('-');
        }

        return st_obj[cssprop] || st_obj[srt_n_s];
    }
    else {
        if (el.currentStyle) {//IE
            if (cssprop == 'float') cssprop = 'styleFloat';
            return el.currentStyle[cssprop];
        }
    }
}
function IAS_ONMOUSEOVER_TABLE2(p_obj,id_not)
{
    if (document.getElementById(id_not) != window.event.srcElement) IAS_ONMOUSEOVER_TABLE(p_obj);
}
function IAS_ONMOUSEOVER_TABLE(p_obj)
{
    if (mas_tr_obj.lastIndexOf(p_obj) == -1)
    {
        tr_obj = null;
        x = p_obj.getElementsByTagName('*');
        mas_style = new Array(x.length);
        for (var i = 0; i < x.length; i++)
        {
            mas_style[i] = getStyleVal(x[i], 'background-color') || x[i].style.backgroundColor;
            x[i].style.backgroundColor = mas_style[i] == "rgb(192, 192, 192)" ? "rgb(247, 141, 8)" : (mas_style[i] == "rgb(211, 218, 245)" ? "rgb(175, 167, 65)" : "rgb(238, 226, 84)");
        }
    }
}

function IAS_ONMOUSEOUT_TABLE2(p_obj, id_not)
{
    if (document.getElementById(id_not) != window.event.srcElement) IAS_ONMOUSEOUT_TABLE(p_obj);
}
function IAS_ONMOUSEOUT_TABLE(p_obj)
{
    if (mas_tr_obj.lastIndexOf(p_obj) == -1 && tr_obj != p_obj && (mas_style != null))
    {
      x = p_obj.getElementsByTagName('*');
      for (var i = 0; i < x.length; x[i].style.backgroundColor = mas_style[i++]);
    }
}

function IAS_ONCLICK_TABLE2(p_obj,id_not)
{
    if (document.getElementById(id_not) != window.event.srcElement) IAS_ONCLICK_TABLE(p_obj);
}
function IAS_ONCLICK_TABLE(p_obj)
{
    var i_p = mas_tr_obj.lastIndexOf(p_obj);
    if (i_p != -1)
    {
        x = mas_tr_obj[i_p].getElementsByTagName('*');
        for (var i = 0; i < x.length; x[i].style.backgroundColor = mas_tr_tag[i_p][i++]);
        mas_tr_obj.splice(i_p, 1);
        mas_tr_tag.splice(i_p, 1);
        tr_obj = p_obj;
    }
    else
    {
        x = p_obj.getElementsByTagName('*');
        for (var i = 0; i < x.length; i++) x[i].style.backgroundColor = x[i].style.backgroundColor == "rgb(238, 226, 84)" ? "rgb(238, 226, 84)" : x[i].style.backgroundColor;
        mas_tr_tag.push(mas_style);
        mas_tr_obj.push(p_obj);
    }
}

function IAS_SELECT_SECTIONS(p_name_e, par)
{
    var m=document.getElementsByName(p_name_e);
    for (var i = 0; i < m.length; i++)
        if (m[i].innerHTML.indexOf(document.title)+1 || m[i].innerHTML.indexOf(par)+1)
            m[i].style.color = 'black';
}
function IAS_GET_HISTORY_SML(id_div_sml) { IAS_GET_HISTORY_SML2(id_div_sml, document.getElementById("P1_ID_SML").value); }
function IAS_GET_HISTORY_SML2(id_div_sml, id_sml) {
    var t_o = document.getElementById(id_div_sml);
    var t_td_s = 'class="t13dataleft"';
    var xmlhttp = getXmlHttp();
    if (xmlhttp == null) return;
    t_res_text = '';
    xmlhttp.open('GET', 'APP_JOURNAL_WEB.GET_HISTORY_SML_JSON?p_id_sml=' + id_sml, true);
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4) {
            if (xmlhttp.status == 200) {
                try {
                    t_res_obj = JSON.parse(xmlhttp.responseText);
                    t_res_text = '<table class="t13Standard" cellpadding="0" cellspacing="0" style="width: 100%;">';
                    t_res_text += '<tbody>';
                    t_res_text += '<tr>';
                    t_res_text += '<td class="t13header">№</td>';
                    t_res_text += '<td class="t13header">Преподаватель до назначения</td>';
                    t_res_text += '<td class="t13header">Преподаватель после назначения</td>';
                    t_res_text += '<td class="t13header">Дата назначения</td>';
                    t_res_text += '</tr>';
                    for (var i = 0; i < t_res_obj.mas.length; i++) {
                        t_res_text += '<tr><td '+ t_td_s +'>'+(i+1)+'</td><td ' + t_td_s + '>' + t_res_obj.mas[i].old_t + '</td><td ' + t_td_s + '>' + t_res_obj.mas[i].new_t + '</td><td ' + t_td_s + '>' + t_res_obj.mas[i].d_sml + '</td></tr>';
                    }
                    t_res_text += '</tbody>';
                    t_res_text += '</table><br>';
                }
                catch (e) {
                    t_res_text = v_error_br;
                }
            }
            else {
                t_res_text = "Ошибка при подключении к серверу";
                if (xmlhttp.responseText) t_res_text += "<br>" + xmlhttp.status + "-" + xmlhttp.responseText;
            }
            t_o.innerHTML = t_res_text
        }
    };
    xmlhttp.send(null);
}
function getXmlHttp() {
    var xmlhttp;
    try {
        xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
    } catch (e) {
        try {
            xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        } catch (E) {
            xmlhttp = false;
        }
    }
    if (!xmlhttp && typeof XMLHttpRequest != 'undefined') {
        xmlhttp = new XMLHttpRequest();
    }
    return xmlhttp;
}

function IAS_LOAD_DETAIL(p_url)
{
    obj = document.getElementById("RES_INFO_AJAX");
    obj.innerHTML = "Идет загрузка...";
    newsrc = IAS_GET_AJAX_TEXT(p_url);
    IAS_Change_Context_AJAX(obj, newsrc);
    obj.scrollIntoView(true);
}
function getUrlDetalicSml(id_sml)
{
    return "app_journal_web.RES_GROUP_MONITORING?p_id_SML=" + id_sml;
}
function LOAD_DETALIC_SML(id_sml)
{
    IAS_LOAD_DETAIL(getUrlDetalicSml(id_sml));
}
function IAS_ONBLUR_JOURNAL(p_obj, id_b_and_stud) { if (p_obj.value != prev_val_e&&p_obj.value) document.getElementById(id_b_and_stud).onclick(); }
function IAS_ONFOCUS_EDIT(p_obj) { prev_val_e = p_obj.value;}
function IAS_FOCUS_NEXT(p_obj,name)
{
	var mas_i=document.getElementsByName(name);
	for (var i=0;i<mas_i.length;i++)
		if(mas_i[i].tabIndex==(p_obj.tabIndex+1))
		{
			mas_i[i].focus();
			break;
		}
}
function IAS_CHECKED_STAT(stat_type, name_radio) {
    var m = document.getElementsByName(name_radio);
    for (var i = 0; i < m.length; i++) 
		if (m[i].value == stat_type) 
			m[i].checked = true;
}