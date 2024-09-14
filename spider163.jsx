
var dialog = new Window("dialog"); 
    dialog.text = "spider163"; 
    dialog.orientation = "column"; 
    dialog.alignChildren = ["center","top"]; 
    dialog.spacing = 10; 
    dialog.margins = 16; 
var edittext1 = dialog.add('edittext {properties: {name: "edittext1"}}'); 
    edittext1.text = "song link/song id"; 
    edittext1.preferredSize.width = 200; 

    // var radiobutton1 = dialog.add("checkbox", undefined, "保存到mysql数据库（这个功能关了，要用的话得自己调试好）");
    // radiobutton1.value = false;
    
    var radiobutton2 = dialog.add("checkbox", undefined, "加载翻译");
    radiobutton2.value = true;

var panel1 = dialog.add("panel", undefined, undefined, {name: "panel1"});
    panel1.text = "合成设置"; 
    panel1.orientation = "column"; 
    panel1.alignChildren = ["left","top"]; 
    panel1.spacing = 10; 
    panel1.margins = 10; 

var input_length = panel1.add('edittext {properties: {name: "input_length"}}'); 
    input_length.text = "1920"; 
    input_length.preferredSize.width = 100;

var input_comp_length;

var input_height = panel1.add('edittext {properties: {name: "input_height"}}'); 
    input_height.text = "1080"; 
    input_height.preferredSize.width = 100;

var input_comp_height;

var input_fra = panel1.add('edittext {properties: {name: "input_fra"}}'); 
    input_fra.text = "30";
    input_fra.preferredSize.width = 100;
var input_comp_fra;


var button1 = dialog.add("button", undefined, undefined, {name: "button1"}); 
    button1.text = "apply"; 

var statictext1 = dialog.add("statictext", undefined, undefined, {name: "statictext1"}); 
statictext1.text = "Drowning鱼"; 


// 获取当前脚本文件的完整路径
var scriptFile = File($.fileName);
// 获取当前脚本所在的目录
var scriptFolder = scriptFile.parent;

    button1.onClick=apply;





function apply(){

    input_comp_length=parseInt(input_length.text);

    input_comp_height=parseInt(input_height.text);

    input_comp_fra=parseInt(input_fra.text); 

    var floder_path=creat_folder();
    // var flag=radiobutton1.value;
    var flag=false;
    var link=edittext1.text;
    var type=get_type(link);
    var values = get_id(link);
    var id=values[0];
    var user_id=values[1];
    if(type===1){//单曲
        song(id,user_id,flag,floder_path);
        alert("单曲合成已创建");
    }
    else if(type===2){//歌单
        playlist(id,user_id,flag,floder_path);
        alert("歌单内单曲合成已创建");
    }
    else if(type===3){//专辑
        album(id,user_id,flag,floder_path);
        alert("专辑内单曲合成已创建");
    }
    else if(type===4){//歌手
        alert("(歌手功能没有做)");
    }
    else if(type===0){
        alert("无效输入");
    }
}

function creat_folder(){
    var project_path;
    try{
        project_path = app.project.file.path;
        var folder = new Folder(project_path);
        project_path = folder.fsName;
        project_path = project_path.replace(/\\/g, "/");
        project_path = "/" + project_path.replace(":", "");

    }
    catch (error){
        alert(error);
        alert("开发者注:当前工程文件没有目录，请保存一下项目（该脚本会在工程目录旁生成相应素材文件夹）");
    }

    // alert(typeof(project_path)+project_path)
    // var project_folder = new Folder(project_path); //父级目录

    var script_folder_path = project_path+'/spider163';
    var script_folder = new Folder(script_folder_path);
    if(script_folder.exists){
    }
    else{
        alert("aep工程文件路径spider163文件夹已创建");
        script_folder.create();
    }
    return script_folder_path;
}
function get_type(link){
    if(link.indexOf("song")!==-1){
        return 1;
    }
    else if(link.indexOf("playlist")!==-1){
        return 2;
    }
    else if(link.indexOf("album")!==-1){
        return 3;
    }
    else if(link.indexOf("artist")!==-1){
        return 4;
    }
    else{
        return 0;
    }
}
function get_id(link){
    pattern=/id=(\d+)(?:&userid=(\d+))?/;
    var match=link.match(pattern);
    var id=match[1];
    var userid=match[2] || null;
    return [id,userid];
}

function playlist(id,user_id,flag,floder_path){
    var playlist_py_path=scriptFolder.fsName+'\\spider163\\playlist.py';
    var command='python '+playlist_py_path+' '+id+' '+flag+' '+floder_path;
    var en_data = system.callSystem(command);
    var de_data = decodeURIComponent(en_data);
    var data=JSON.parse(de_data);
    var ids=data['ids'].split('/');
    for(var i=0;i<ids.length;i++){
        id=ids[i];
        if(id){
            var song_comp=creat_song_comp(data[id]);
        }
    }
}
function album(id,user_id,flag,floder_path){

    var album_py_path=scriptFolder.fsName+'\\spider163\\album.py';

    var command='python '+album_py_path+' '+id+' '+flag+' '+floder_path;

    var en_data = system.callSystem(command);

    var de_data = decodeURIComponent(en_data);

    var data=JSON.parse(de_data);

    var ids=data['ids'].split('/');
    for(var i=0;i<ids.length;i++){
        id=ids[i];
        if(id){
            var song_comp=creat_song_comp(data[id]);
        }
    } 
}

function song(id,user_id,flag,floder_path){
    // var song_py_path='D:/\Adobe/\AE_script/\spider163/\song.py';
    var song_py_path=scriptFolder.fsName+'\\spider163\\song.py';
    // alert('D:/\Adobe/\AE_script/\spider163/\song.py');
    // alert(song_py_path);
    var command = 'python '+song_py_path+' '+id+' '+flag+' '+floder_path;
    // alert("2"+song_py_path+' '+id+' '+flag+' '+floder_path);
    var en_data = system.callSystem(command);
    // alert("3"+en_data);
    var de_data = decodeURIComponent(en_data);
    // alert("4"+de_data);
    var data=JSON.parse(de_data);
    // alert("5")
    var song_comp=creat_song_comp(data);
    // alert("6");
}

function creat_song_comp(data){
    var comp=comp_is_exists(data['name']);
    try{
        var img=import_img(data,comp);//导入图片
    }
    catch (error){
        alert(error);
    }
    var lines = data['lrc'].split('\n');
    var text_layer;
    for (var i = 0; i < lines.length; i++) {
        var line = lines[i];
        if(line)
            text_layer=creat_text(comp,line,text_layer,[0,comp.height/2]);
    }
    if(radiobutton2.value){
        var text_layer_2;
        var lines = data['lyric'].split('\n');
        for (var i = 0; i < lines.length; i++) {
            var line = lines[i];
            if(line)
                text_layer_2=creat_text(comp,line,text_layer_2,[0,comp.height/2+200]);
        }
    }
    return comp;
    function comp_is_exists(name){
        for (var i = 1; i <= app.project.numItems; i++) {
            var comp = app.project.item(i);
            if(comp.name==name){
              return comp;
            }
          }
        //   alert(input_comp_fra);
          comp=app.project.items.addComp(name, input_comp_length, input_comp_height, 1, 300, input_comp_fra);
          return comp;
    }
    function creat_text(comp,line,last_text,layer_position){
        var sta_t=0;
        var pattern = /\[(\d{2}):(\d{2})\.(\d{2,3})?\](.*)/;
        var match = line.match(pattern);
        if (match) {
          var sta_m = parseInt(match[1],10); 
          var sta_s = parseInt(match[2],10); 
          var sta_ms = match[3];
          var textContent = match[4];
      
          if (sta_ms.length === 2) {
            sta_t=sta_m*60+sta_s+parseInt(sta_ms,10)*0.01;
          } else if (sta_ms.length === 3) {
            sta_t=sta_m*60+sta_s+parseInt(sta_ms,10)*0.001;
          }
        } else {
          sta=0;
          textContent='Error';
        }
        sta_time=fra_to_fra(comp,sta_t);
        if(last_text){
          last_text.outPoint=sta_time;//fra_to_fra(comp,sta_t,1);
        }
        var textLayer = comp.layers.addText();
        textLayer.startTime = sta_time;
        textLayer.property("Source Text").setValue(textContent);
        textLayer.position.setValue(layer_position);
        return textLayer;
    }
    function fra_to_fra(comp,sta_t){
        sta_fra=Math.round(sta_t*comp.frameRate);
        return (sta_fra/comp.frameRate*1.0);
    }
    function import_img(data,comp){
        var project = app.project; // 获取当前项目
        var img = new ImportOptions(File(data['music_img']));
        var footageItem = project.importFile(img); // 导入素材文件
        footageItem.name=data['name'];
        var layer = comp.layers.add(footageItem); // 将素材添加为合成的图层
        layer.name = footageItem.name; // 设置图层名称与素材文件名相同
        return layer;
    }
}

dialog.show();