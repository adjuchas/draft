<template>
  <div  class="main">
    <div class="navbar">
<!--      导航栏部分-->
      <p class="title">易班城市绿洲报征稿平台</p>
          <p class="message"> 你好，{{this.$store.state.user.name}}
<!--            页面渲染元素残留问题，待修复-->
            <svg @click="logout" class="icon" viewBox="0 0 1024 1024"  xmlns="http://www.w3.org/2000/svg"  width="20" height="16"><path d="M585.142857 914.285714H219.428571c-58.514286 0-109.714286-51.2-109.714285-109.714285V219.428571c0-58.514286 51.2-109.714286 109.714285-109.714285h365.714286c58.514286 0 109.714286 51.2 109.714286 109.714285v73.142858c0 21.942857-14.628571 36.571429-36.571429 36.571428s-36.571429-14.628571-36.571428-36.571428V219.428571c0-21.942857-14.628571-36.571429-36.571429-36.571428H219.428571c-21.942857 0-36.571429 14.628571-36.571428 36.571428v585.142858c0 21.942857 14.628571 36.571429 36.571428 36.571428h365.714286c21.942857 0 36.571429-14.628571 36.571429-36.571428v-73.142858c0-21.942857 14.628571-36.571429 36.571428-36.571428s36.571429 14.628571 36.571429 36.571428v73.142858c0 58.514286-51.2 109.714286-109.714286 109.714285z" ></path><path d="M804.571429 650.971429c-7.314286 0-21.942857 0-29.257143-7.314286-14.628571-14.628571-14.628571-36.571429 0-51.2L855.771429 512l-80.457143-80.457143c-14.628571-14.628571-14.628571-36.571429 0-51.2s36.571429-14.628571 51.2 0l102.4 102.4c14.628571 14.628571 14.628571 36.571429 0 51.2l-102.4 102.4c0 14.628571-14.628571 14.628571-21.942857 14.628572z" ></path><path d="M877.714286 548.571429H512c-21.942857 0-36.571429-14.628571-36.571429-36.571429s14.628571-36.571429 36.571429-36.571429h365.714286c21.942857 0 36.571429 14.628571 36.571428 36.571429s-14.628571 36.571429-36.571428 36.571429z" ></path></svg>
          </p>
    </div>

    <div style="padding-top: 58px">
<!--      主题选择-->
    请先选择上传文件类型： <el-cascader
      v-model="file_type"
      :options="optionsthems"
      placeholder="选择文件类型"
  >
  </el-cascader>
<!--      平台使用规则-->
    <el-tooltip class="item"  effect="light"  placement="top-start">
      <div slot="content">
        <p>1、上传文件前请先选择上传的作品主题，上传成功的文件会在提交记录的表格中显示，同一主题下仅最后一次提交有效；</p>
        <p>2、压缩包文件上传仅支持zip格式；</p>
        <p>3、批量下载功能需要在表格中选定指定的文件进行下载；</p>
        <p>4、使用过程中，如遇到问题请联系管理员：<a href="">mazuxian1202@gmail.com</a></p>
      </div>
      <el-button  icon="el-icon-info" :autofocus="false">平台使用规则</el-button>
    </el-tooltip>
<!--上传部分-->
    <el-upload
        style="margin-top: 30px;"
        class="upload-demo"
        multiple
        drag
        :data="{file_type:file_type[1],access_token:this.$store.state.token}"
        show-file-list
        action="https://csxy-yiban.cn/api/app215/stu/upload_file/"
        :on-success=" filesuccess"
        :before-upload="beforupload"
        name="myfile"
        :limit="30"
        :on-error="submiterror"
    >
      <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
      <div slot="tip" class="el-upload__tip">只能上传doc、docx或zip文件，且文件名长度不超过15个字</div>
    </el-upload>

<!--    提交记录表格-->
    <el-table @selection-change="change"
              ref="Stable"
              show-header
              style="margin:  auto;width: 690px;"
              :data="filelog"
    >
      <el-table-column   type="selection" width="55"></el-table-column>
      <el-table-column  fixed label="作品名称" width="150" prop="upload_name" ></el-table-column>
      <el-table-column  prop="create_time" label="日期" width="150"></el-table-column>
      <el-table-column  label="作品主题" width="200" prop="upload_type"></el-table-column>
      <el-table-column prop="upload_state" label="审核状态" width="120"></el-table-column>
    </el-table>
    <el-button style="margin: 30px 0 30px;"  icon="el-icon-download" v-prevent-click @click="downloads">批量下载</el-button>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "navbar",
  props:['filelog'],
  data(){
    return {
      //表格选中记录
      recodes:[],
      //主题选题，第二版要实现向服务器获取选择的信息
      optionsthems:[
        {
          value:"doc",
          label:'诗歌文档上传',
          children:[{
            value:1,
            label:'中国故事'
          },
            {
              value: 2,
              label:'时代印记'
            },
            {
              value: 3,
              label: "青春风采"
            }
          ],
        },
        {
          value:'zip',
          label: "摄影压缩包上传",
          children:[{
            value:4,
            label:'中国故事'
          },
            {
              value: 5,
              label:'时代印记'
            },
            {
              value: 6,
              label: "青春风采"
            }
          ]
        }
      ],
      file_type:[],//选中的主题
      file_log:[]//获取提交记录
    }
  },
  methods:{
    beforupload(file){//提交前检验
      if (file.size/1024/1024>40){//限制文件大小
        this.$message.warning('上传的文件不能大于40M');
        return false;
      }
      const options=this.file_type;
      if (options.length<1){//未选中主题
        this.$message.warning('请选择上传的文件类型');
        return false;
      }
      if(options[0]==='zip') {
        const name=file.name.replace(/.zip/,"");
        const iszip = file.name.endsWith('.zip')
        if (!iszip) {
          this.$message.error('只支持上传zip格式压缩包');
          return false;
        }
        else if (name.length>15){
          this.$message.error('文件名长度不能超过15个字符');
          return  false;
        }
       return true
     }
     if (options[0]==='doc'){
      const isDOC = file.name.endsWith('.doc') || file.name.endsWith('.docx');
      const name=file.name.replace(/.docx|.doc/,"");
      if(!isDOC){
        this.$message.error('只支持上传doc、docx格式文档');
        return false;
      }
      else if (name.length>15){
        this.$message.error('文件名长度不能超过15个字符');
        return  false;
      }
     return true;
    }
     },
    filesuccess(response){//提交成功
      if (response.message==='success'){
        this.$message.success("成功上传，请耐心等待审核结果");
       this.$emit('fileupload',this.$store.state.token)
      }
      else
      this.$message.error(response.message+"，请重新上传");
    },
    submiterror(){//提交失败
      this.$message.error("上传超时,请联系管理员");
    },
      change(val){//表格选择
        this.recodes=[];
        val.forEach(i=>{
         this.recodes.push(i.recode_id);
       })
      },
    downloads(){//批量下载

      if(this.recodes.length<1){
        this.$message.warning("请在提交记录中选择文件")
        return false
      }
    else{
      axios.post('https://csxy-yiban.cn/api/app215/stu/download/',{
        "access_token":this.$store.state.token
        , "recodes":this.recodes
      }).then(res=>{
        window.location.href=res.data.uri;
      })
    }
    },
    logout(){//登出
      axios.post('https://csxy-yiban.cn/api/app215/oauth/logout/',{
        "access_token":this.$store.state.token
        ,"uid":localStorage.getItem("215_uid")
      }).then(res=>{
        if (res.data.message==='success'){
          localStorage.clear();//清理数据
          sessionStorage.clear();
          location.reload();
        }
        else{
          console.log(res.data);
          this.$message.error("登出失败，请联系管理员");}
      }).catch(function (err){
        this.$message.error("登出失败，请联系管理员");
        console.log(err);
      })
    },
  }
}
</script>

<style scoped>

.navbar{
  margin-top: -15px;
  width: 100%;
  border-radius:10px;
  background-color: rgba(71, 229, 120, 0.49);
  height: 100px;
  box-shadow: 6px 20px 45px -12px rgba(98 ,109, 100, 0.75);
  -webkit-box-shadow: 6px 20px 45px -12px rgba(98 ,109, 100, 0.75);
  -moz-box-shadow: 6px 20px 45px -12px rgba(98 ,109, 100, 0.75);
}
.icon{

  position: relative;
  top: 2px;
  left: 0;
  cursor: pointer;
}
.title{
  position: relative;
  top: 20px;
  text-shadow:5px 7px 4px rgba(42, 177 ,84, 0.64);
  /*border-bottom: blue 3px solid ;*/
  color: rgba(6, 103, 0, 0.84);
  font-size:30px ;
  font-family: "Microsoft YaHei UI",serif;
}
.navbar .message{
  position:absolute;
  text-shadow:0 0 1px #868686; color: rgba(31 ,131, 67, 0.94);
  /*border-bottom: blue 3px solid ;*/
  top: 70px;
  right: 20px;
}
</style>