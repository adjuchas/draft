<template >
<div>
 <el-container>
   <el-header >绿洲征文管理系统</el-header>
   <el-main>
     <el-cascader
         v-model="filetype"
         placeholder="请选择主题"
         filterable
        :props="props"
        :options="themeData"
     ></el-cascader>
     <el-button v-prevent-click style="margin-left: 15px;" type="primary" icon="el-icon-s-data" @click="changeView">筛选</el-button>
     <el-button v-prevent-click style="margin-left: 15px;" @click="getAllinfo" icon="el-icon-refresh" >重置</el-button>
     <el-divider></el-divider>

     <el-table
         @selection-change="change"
                class="tableClass"
                :data="allrecodes.slice((currentPage-1)*pagesize,currentPage*pagesize)"
                max-height="670px" width="80%">
       <el-table-column fixed  type="selection" width="55"></el-table-column>
       <el-table-column   width="120" label="作品ID" prop="recode_id"></el-table-column>
       <el-table-column label="提交日期"  sortable width="200" prop="create_time"></el-table-column>
       <el-table-column width="150" label="学号" sortable prop="stuid"></el-table-column>
       <el-table-column width="200" label="作品名称" prop="upload_name"></el-table-column>
       <el-table-column width="200" label="作品类型" prop="upload_type"></el-table-column>
       <el-table-column width="120" label="审核状态" align="center" prop="upload_state"
                        :filter-method="filterTag"
                        :filter-multiple="false"
                        column-key="upload_state"
                        :filters="[{text:'待审核',value:'待审核'},{text:'审核通过,待征稿',value:'审核通过,待征稿'},{text:'已被征稿',value:'已被征稿'},{text:'审核不通过',value:'审核不通过'}]"
       ></el-table-column>
       <el-table-column
           fixed="right"
           label="更改状态"
           width="120">
         <template slot-scope="scope">
           <el-select v-model="scope.row.upload_state" size="mini" @change="v=>changeState(v,scope.row.recode_id)" default-first-option>
             <el-option
                 v-for="item in  sateSeletions"
                 :key="item.value"
                 :label="item.label"
                 :value="item.value"
             ></el-option>
           </el-select>
         </template>
       </el-table-column>
     </el-table>

     <el-pagination
         style="text-align: center"
         @current-change="handleCurrentChange"
         layout="total,sizes,prev, pager, next,jumper"
         :page-size="this.pagesize"
         :page-sizes="[10,50,100,400]"
         @size-change="handleSizeChange"
         :current-page="this.currentPage"
         :total="allrecodes.length">
     </el-pagination>
     <el-popconfirm
         icon="el-icon-info"
         title="确认保存数据？"
          @confirm="saveState"
     >
       <el-button style="margin-left: 15px;" type="primary" slot="reference" icon="el-icon-finished" >保存更改</el-button>

     </el-popconfirm>
     <el-button v-prevent-click style="margin: 10px" @click="downloads" icon="el-icon-download" >批量下载</el-button>
 </el-main>

 </el-container>
</div>
</template>

<script>
import axios from "axios";


export default {
  name: "home",
created() {
    this.getAllinfo();
},
  data(){
    return{
      allrecodes:[],//全部的数据表
      pagesize:10,//条目数量
      currentPage:1,//当前页
      props:{multiple:true},//选择器多选
      filetype:[],//筛选返回的结果
      selectValue:[],//审核状态返回结果
      download_recodes:[],//批量下载数组
      themeData:[//主题筛选
        {
          value:"doc",
          label:'文本文档',
          children:[
            {
              value:1,
              label:'中国故事'
            },
            {
              value:2,
              label:'时代印记'
            },
            {
              value:3,
              label:'青春风采'
            }
          ]
        },
        {
          value: "zip",
          label: '压缩包',
          children: [
            {
              value: 4,
              label: '中国故事'
            },
            {
              value: 5,
              label: '时代印记'
            },
            {
              value: 6,
              label: '青春风采'
            }
          ]
        }
        ],
          sateSeletions:[//审核状态
            {
              value:"审核不通过",
              label:"审核不通过"
            },
            {
              value: "审核通过",
              label: "审核通过"
            },{
              value: "文档通过征稿",
              label: "文档通过征稿"
            },
            {
              value: '待审核',
              label: '待审核'
            }
          ],
      changeStateArrey:[],
  }
  },
  methods:{
    getAllinfo() {
      let that = this;
        this.filetype = null;
        axios.get('https://csxy-yiban.cn/api/app215/admin_215/selectall/', {
          params: {"access_token":'2889616a72cdef1f3bced725c29be7a5b0710cb0'}
        }).then(res => {
          console.log(res.data);
          that.allrecodes = res.data.recodes;
        })
      },
    changeView() {//筛选数据用
      if (this.filetype==null){
        this.$message.warning("请选择主题")
        return false
      }
      axios.post('http://120.25.121.177:443/api/admin_215/type_select/',{
        "access_token":'2889616a72cdef1f3bced725c29be7a5b0710cb0',"select_type":this.filetype
      }).then((res)=>{
        this.allrecodes=res.data.recodes
      })
      },
    change(val){//获取数据表选中行信息
      this.download_recodes=[];
      for (let i in val){
        this.download_recodes[i]=val[i].recode_id;
      }
    },
    filterTag(value,row){//页码条目
      return row.upload_state===value
    },
    changeState(e,a){//改变状态的记录
      let temp={};
      temp[a]=e;
      this.changeStateArrey.push(temp);
      console.log(this.changeStateArrey);
    },
    saveState(){//提交状态
      if (this.changeStateArrey.length<1){
        this.$message.warning("从未改变过文件审核状态");
        return false;
      }
      axios.post('https://csxy-yiban.cn/api/app215/admin_215/set_state/',{
        "access_token":'e64467e25e63a28c5ca0ffad3ec9ccfdfc2a198a',
        "set_recode":this.changeStateArrey
      }).then((res)=>{
        if (res.data.message==="success")
          this.$message.success("保存成功")
        {
          console.log(res.data.message);
        }
      }).catch(e=>{
        console.log(e);
        this.$message.error("服务器内部错误")
      })
    },
    downloads(){//批量下载
      let d =this.download_recodes;
      if (d.length<1){//判断有无选择
        this.$message.warning('未选择文件');
        return false;
      }
      else
        axios.post('https://csxy-yiban.cn/api/app215/admin_215/downloads/',{
          "access_token":'2889616a72cdef1f3bced725c29be7a5b0710cb0',"recodes":this.download_recodes
        }).then((res)=>{
          window.location.href=res.data.uri
        })
    },
    handleCurrentChange(e){//改变页数
      this.currentPage=e;
    },
    handleSizeChange(e){//改变页码条目
      this.pagesize=e;
    },
      test(){
        this.$refs.filterTable.clearFilter();
      }
  }
}
</script>

<style scoped>
.el-header {
  border-radius: 10px;
  border: 1px rgba(30, 194, 210, 0.85) solid;
  background-color: rgba(62, 175, 45, 0.25);
  color: #333;
  text-align: center;
  line-height: 50px;
}
.el-main{
  margin: 20px;
  border: lightsteelblue solid;
}
.tableClass{
  margin:5px auto;text-align: center;border: lightsteelblue solid 1px;
}
</style>