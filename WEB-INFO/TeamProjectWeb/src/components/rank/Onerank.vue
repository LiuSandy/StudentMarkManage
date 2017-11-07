<template>
  <div>
    <Dropdown @on-click="getSub" style="margin-left: 20px">
      <Button type="primary">选择属性
        <Icon type="arrow-down-b"></Icon>
      </Button>
      <Dropdown-menu slot="list">
        <Dropdown-item name="安卓">安卓</Dropdown-item>
        <Dropdown-item name="C语言">C语言</Dropdown-item>
        <Dropdown-item name="Python">Python</Dropdown-item>
        <Dropdown-item name="快速建站">快速建站</Dropdown-item>
        <Dropdown-item name="Linux">Linux</Dropdown-item>
        <Dropdown-item name="网络">网络</Dropdown-item>
      </Dropdown-menu>
    </Dropdown>
    <br><br>
    <Table border :columns="columns" :data="data"></Table>
    <br>
    <Page :total="Number(total)" :current="1" show-elevator @on-change="changePage"></Page>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        total: '',
        alldata: [],
        columns: [
          {
            title: '学号',
            key: 'studentId'
          },
          {
            title: '姓名',
            key: 'name'
          },
          {
            title: '课程名',
            key: 'subName'
          },
          {
            title: '课程分数',
            key: 'subScore'
          },
          {
            title: '排名',
            key: 'grade'
          },
          {
            title: '操作',
            key: 'action',
            width: 150,
            align: 'center',
            render: (h, params) => {
              return h('div', [
                h('Button', {
                  props: {
                    type: 'primary',
                    size: 'small'
                  },
                  style: {
                    marginRight: '5px'
                  },
                  on: {
                    click: () => {
                      this.show(params.index)
                    }
                  }
                }, '查看'),
                h('Button', {
                  props: {
                    type: 'info',
                    size: 'small',
                    icon: 'stats-bars'
                  },
                  on: {
                    click: () => {
                      this.$router.push({name: 'saleShow', params: {id: `${this.data1[params.index].sale_nbr}`}})
                    }
                  }
                }, '详情')
              ])
            }
          }
        ],
        data: []
      }
    },
    mounted () {
      this._selectRank('安卓')
    },
    methods: {
      getSub (name) {
        this._selectRank(name)
      },
      _selectRank (name) {
        this.$http.get('/selectRank', {params: {'q': name}}).then(response => {
          let data = response.data
          this.total = response.data.length
          let tempData = []
          for (let i in data) {
            let item = {
              studentId: data[i][0],
              name: data[i][1],
              subName: data[i][2],
              subScore: data[i][3],
              grade: Number(i) + 1
            }
            tempData.push(item)
            if (tempData.length === 10) {
              this.alldata.push(tempData)
              tempData = []
            }
          }
          console.log(tempData)
          this.data = this.alldata[0]
        })
      },
      changePage (event) {
        if (this.alldata.length >= event) {
          this.data = this.alldata[event - 1]
        }
      },
      show (index) {
        this.$Modal.info({
          title: '学生成绩详情',
          content: `sale_nbr：${this.data1[index].sale_nbr}<br>cnt：${this.data1[index].cnt}<br>round：${this.data1[index].round}<br>in_degree：${this.data1[index].in_degree}<br>out_degree：${this.data1[index].out_degree}<br>page_rank：${this.data1[index].PageRank}`
        })
      }
    }
  }
</script>
