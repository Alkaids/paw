<template>
  <div class="page-container">
    <div class="left-sidebar">
      <el-menu class="el-menu-vertical" :collapse="isCollapse" background-color="#304156"
               text-color="#bfcbd9"
               active-text-color="#409EFF" :router="isRouter">
        <el-submenu index="1">
          <template slot="title">
            <i class="el-icon-menu"></i>
            <span slot="title">主菜单</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="/main">总览</el-menu-item>
            <el-menu-item index="/schedule">爬虫调度</el-menu-item>
            <el-menu-item index="1-3">爬取日志</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <el-submenu index="2">
          <template slot="title">
            <i class="el-icon-upload"></i>
            <span slot="title">部署</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="/setting">设置</el-menu-item>
            <el-menu-item index="/upload_project">上传项目</el-menu-item>
            <el-menu-item index="/deploy_local_project">部署本地项目</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <el-menu-item index="3">
          <i class="el-icon-edit"></i>
          <span slot="title">开发者</span>
        </el-menu-item>
        <el-menu-item index="4">
          <i class="el-icon-question"></i>
          <span slot="title">帮助</span>
        </el-menu-item>
      </el-menu>
    </div>
    <div class="nav-bar">
      <el-menu mode="horizontal">
        <i class="fa fa-paw fa-3x" aria-hidden="true" style="float: left; margin-left: 20px;"></i>
        <a style="float: left; margin-left: 20px;line-height: 60px">PAW</a>
        <div class="right-menu">
          <el-menu-item index="1" class="right-menu-item">消息</el-menu-item>
          <el-dropdown class="avatar-container right-menu-item" trigger="click">
            <div class="avatar-wrapper">
              <i class="fa fa-user" aria-hidden="true"></i>
              <i class="el-icon-caret-bottom">用户</i>
            </div>
            <el-dropdown-menu slot="dropdown">
              <router-link to="/">
                <el-dropdown-item>
                  注销
                </el-dropdown-item>
              </router-link>
              <a target='_blank' href="https://github.com/PanJiaChen/vue-element-admin/">
                <el-dropdown-item>
                  github
                </el-dropdown-item>
              </a>
            </el-dropdown-menu>
          </el-dropdown>
        </div>
      </el-menu>
    </div>
    <div class="content-container">
      <!--<transition name="el-fade-in-linear">-->
        <router-view></router-view>
      <!--</transition>-->
    </div>
  </div>
</template>

<script>

  export default {
    data() {
      return {
        isCollapse: false,
        isRouter: true
      }
    }
  }
</script>

<style scoped>
  .el-menu-vertical {
    width: 13.5%;
    height: 100%;
    text-align: left;
    position: fixed;
    left: 0;
    top: 0;
  }

  .page-container {
    width: 100%;
    height: 100%;
  }

  .left-sidebar {
    max-width: 20%;
  }

  .nav-bar {
    margin-left: 13.5%;
  }

  .content-container {
    margin-left: 210px;
  }

  .right-menu {
    float: right;
  }

  .right-menu-item {
    display: inline-block;
  }
</style>
