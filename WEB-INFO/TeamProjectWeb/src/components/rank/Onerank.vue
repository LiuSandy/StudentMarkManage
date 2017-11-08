<template>
  <div>
    <Row>
      <Col span="6">
      <Select v-model="model" clearable style="width:200px">
        <Option v-for="item in cityList" :value="item.value" :key="item">{{ item.label }}</Option>
      </Select>
      </Col>
      <Col span="9" offset="1">
      分数段：
      <Input-number :max="100" :min="1" :step="5" v-model="value1"></Input-number>
      ——
      <Input-number :max="100" :min="1" :step="5" v-model="value2"></Input-number>
      </Col>
      <Button type="primary" offset="1" @click="getParam">查询</Button>
    </Row>
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
        value1: 0,
        value2: 10,
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
        data: [],
        cityList: [
          {
            value: '安卓',
            label: '安卓'
          },
          {
            value: 'C语言',
            label: 'C语言'
          },
          {
            value: 'Python',
            label: 'Python'
          },
          {
            value: 'Linux',
            label: 'Linux'
          },
          {
            value: '快速建站',
            label: '快速建站'
          },
          {
            value: '网络',
            label: '网络'
          }
        ],
        model: ''
      }
    },
    mounted () {
      this._selectRank('安卓')
    },
    methods: {
      getParam () {
        console.log(this.model8)
        let param = {
          startScore: this.value1,
          endScore: this.value2,
          subject: this.model
        }
        this._selectRank(param)
        console.log('HELLO WORLD')
      },
      _selectRank (param) {
        this.$http.get('/getRegion', {
          params: {
            startScore: param.startScore,
            endScore: param.endScore,
            subject: param.subject
          }
        }).then(response => {
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
