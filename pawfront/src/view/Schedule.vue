<template>
  <div class="main-content">
    <vue-topprogress ref="topProgress"></vue-topprogress>
    <div class="button-tool">
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
          min-width="23%"
          header-align="center"
        />
        <el-table-column
          label="路径"
          prop="path"
          min-width="40%"
          header-align="center"
        />
        <el-table-column
          label="最新部署时间"
          min-width="20%"
          header-align="center">
          <template slot-scope="scope">
            <el-popover trigger="hover" placement="top">
              <el-table
                :data="scope.row.versions"
                style="width: 100%">
                <el-table-column
                  prop="version"
                  label="版本"
                  width="120">
                </el-table-column>
                <el-table-column
                  prop="versionTime"
                  label="版本部署时间"
                  width="250">
                </el-table-column>
              </el-table>
              <div slot="reference" class="name-wrapper">
                <el-tag size="medium">{{ scope.row.lastVersionTime }}</el-tag>
              </div>
            </el-popover>
          </template>
        </el-table-column>
        <el-table-column label="部署" header-align="center" min-width="20%">
          <template slot-scope="scope">
            <el-button
              type="primary"
              size="mini"
              @click="handleSchedule(scope.row)"
            >调度
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>
<script>
  import {
    listdefinedprojects,
    listversionsbyprojectname,
    listprojects
  } from '../store/api'
  import {timeStampFormat} from '../utils/timeUtils'

  export default {
    name: 'DepoyLocalProject',
    data() {
      return {
        formLabelWidth: '200px',
        projects: [],
        versionList: {}
      }
    },
    methods: {
      // 加载定义好的项目
      listDefinedProjects() {
        let param = {}
        param.ispaw = true
        listdefinedprojects(param).then(res => {
          this.projects = res.data
          for (let p of this.projects) {
            p.isDeploy = false
            p.lastVersionTime = '尚未部署'
            p.versions = []
          }
          this.listVersionsByProjectname()
        })
      },
      handleSchedule(project) {

      },
      listVersionsByProjectname() {
        listprojects().then(res => {
          if (res.projects.length === 0) {
            this.$refs.topProgress.done()
          } else {
            for (let project of res.projects) {
              let param = {}
              param.name = project
              this.versionList[project] = []
              listversionsbyprojectname(param).then(res => {
                for (let ver of res.versions) {
                  this.versionList[project].push(ver)
                }
                this.addVersionsToProject(project)
                this.$refs.topProgress.done()
              })
            }
          }
        }).catch(err => {
          console.log(err)
        })
      },
      addVersionsToProject() {
        for (let i in this.versionList) {
          for (let p of this.projects) {
            if (i === p.name) {
              p.isDeploy = true
              p.versions = []
              p.name = p.name + '199999'
              p.name = p.name.replace('199999', '')
              for (let v of this.versionList[i]) {
                let version = {}
                version.version = v
                version.versionTime = timeStampFormat(v)
                p.versions.push(version)
              }
              p.lastVersionTime = timeStampFormat(Math.max(...this.versionList[i]))
            }
          }
        }
      }
    },
    mounted() {
      this.$refs.topProgress.start()
      this.listDefinedProjects()
    }
  }
</script>

<style scoped>
  .left-title {
    text-align: left !important;
    margin-left: 2%;
  }

  .main-content {
    border: 1px solid #ebebeb;
    border-radius: 3px;
    margin-top: 5px;
  }

  .button-tool {
    text-align: left;
    margin: 1% 0;
  }
</style>
