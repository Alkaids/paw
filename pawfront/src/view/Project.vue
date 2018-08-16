<template>
  <div class="main-content">
    <div class="button-tool">
      <el-button type="primary" size="mini"
                 @click="dialogAddFormVisible = true" style="margin-left: 10px">新增项目
      </el-button>
    </div>
    <h4 class="left-title"> 项目列表
    </h4>
    <div class="pending-table">
      <el-table
        :data="projects"
        style="width: 100%">
        <el-table-column
          label="名称"
          sortable
          prop="name"
          min-width="10%"
          header-align="center"
        />
        <el-table-column
          label="备注"
          prop="memo"
          min-width="25%"
          header-align="center"
        />
        <el-table-column
          label="路径"
          prop="path"
          min-width="50%"
          header-align="center"
        />
        <el-table-column label="操作" header-align="center" min-width="15%">
          <template slot-scope="scope">
            <el-button
              size="mini"
              @click="handleEdit(scope.row)">编辑
            </el-button>
            <el-button
              size="mini"
              type="danger"
              @click="handleDelete(scope.row)">删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-dialog title="新建项目" :visible.sync="dialogAddFormVisible">
        <el-form :model="project">
          <el-form-item label="项目名称" :label-width="formLabelWidth">
            <el-tooltip class="item" effect="dark" content="Scrapy.cfg 中的project的值" placement="right">
              <el-input v-model="project.name" auto-complete="off"></el-input>
            </el-tooltip>
          </el-form-item>
          <el-form-item label="项目备注" :label-width="formLabelWidth">
            <el-input v-model="project.memo" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="项目路径" :label-width="formLabelWidth">
            <el-tooltip class="item" effect="dark" content="项目所在路径，路径下应有Scrapy.cfg文件" placement="right">
              <el-input v-model="project.path" auto-complete="off"></el-input>
            </el-tooltip>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogAddFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="saveProject">确 定</el-button>
        </div>
      </el-dialog>
      <el-dialog title="编辑项目" :visible.sync="dialogEditFormVisible">
        <el-form :model="project">
          <el-form-item label="id" :label-width="formLabelWidth">
            <el-input v-model="project.id" auto-complete="off" :disabled="true"></el-input>
          </el-form-item>
          <el-form-item label="项目名称" :label-width="formLabelWidth">
            <el-tooltip class="item" effect="dark" content="Scrapy.cfg 中的project的值" placement="right">
              <el-input v-model="project.name" auto-complete="off"></el-input>
            </el-tooltip>
          </el-form-item>
          <el-form-item label="项目备注" :label-width="formLabelWidth">
            <el-input v-model="project.memo" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="项目路径" :label-width="formLabelWidth">
            <el-tooltip class="item" effect="dark" content="项目所在路径，路径下应有Scrapy.cfg文件" placement="right">
              <el-input v-model="project.path" auto-complete="off"></el-input>
            </el-tooltip>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogEditFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="saveProject">确 定</el-button>
        </div>
      </el-dialog>
    </div>
  </div>
</template>
<script>
  import {
    listdefinedprojects,
    saveproject,
    updateproject,
    getproject,
    delproject
  } from '../store/api'

  export default {
    name: 'Project',
    data() {
      return {
        dialogAddFormVisible: false,
        dialogEditFormVisible: false,
        project: {},
        formLabelWidth: '200px',
        projects: []
      }
    },
    mounted() {
      this.listDefinedProjects()
    },
    methods: {
      // 加载定义好的项目
      listDefinedProjects() {
        let param = {}
        param.ispaw = true
        listdefinedprojects(param).then(res => {
          this.projects = res.data
        })
      },
      // 保存项目
      saveProject() {
        if (this.project.id && this.project.id > 0) {
          let param = {}
          param.ispaw = true
          param.id = this.project.id
          param.path = this.project.path
          param.name = this.project.name
          param.memo = this.project.memo
          updateproject(param).then(res => {
            this.dialogEditFormVisible = false
            this.listDefinedProjects()
            this.$notify({
              title: '成功',
              message: res.msg
            })
            this.listDefinedProjects()
          }).catch(err => {
            console.log(err)
          })
        } else {
          let param = {}
          param.ispaw = true
          param.path = this.project.path
          param.name = this.project.name
          param.memo = this.project.memo
          saveproject(param).then(res => {
            this.dialogAddFormVisible = false
            this.listDefinedProjects()
            this.$notify({
              title: '成功',
              message: res.msg
            })
            this.listDefinedProjects()
          }).catch(err => {
            console.log(err)
          })
        }
      },
      // 编辑项目
      handleEdit(row) {
        let param = {}
        param.ispaw = true
        param.id = row.id
        getproject(param).then(res => {
          this.project = res.data
          this.dialogEditFormVisible = true
        }).catch(err => {
          console.log(err)
        })
      },
      // 删除项目
      handleDelete(row) {
        this.$confirm('是否确认删除？', '确认信息', {
          distinguishCancelAndClose: true,
          confirmButtonText: '删除',
          cancelButtonText: '放弃删除'
        })
          .then(() => {
            let param = {}
            param.ispaw = true
            param.id = row.id
            delproject(param).then(res => {
              this.$notify({
                title: '成功',
                message: res.msg
              })
              this.listDefinedProjects()
            }).catch(err => {
              console.log(err)
            })
          })
          .catch(action => {
          })
      }
    }
  }
</script>

<style scoped>
  .button-tool {
    text-align: left;
    margin: 1% 0;
  }

  .main-content {
    border: 1px solid #ebebeb;
    border-radius: 3px;
    margin-top: 5px;
  }
</style>
