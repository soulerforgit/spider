<template>
  <div class="app">
    <section class="code_edit">

      <codemirror ref="myCm"
                  v-model="code"
                  :options="cmOptions"
                  @ready="onCmReady"
                  @focus="onCmFocus"
                  @input="onCmCodeChange">
      </codemirror>
      <button style="align-self: flex-end" @click="submit_code">提交</button>
    </section>
    <section class="task_show">{{code}}</section>
    <section class="response_show">{{response}}</section>
  </div>
</template>

<script>
  import {codemirror} from 'vue-codemirror'

  // require styles
  import 'codemirror/lib/codemirror.css'
  import 'codemirror/lib/codemirror.js'

  // language
  import 'codemirror/mode/python/python.js'

  // require active-line.js
  import'codemirror/addon/selection/active-line.js'
  // closebrackets
  import'codemirror/addon/edit/closebrackets.js'

  // theme css
  import 'codemirror/theme/base16-light.css'

  // keyMap
  import'codemirror/mode/clike/clike.js'
  import'codemirror/addon/edit/matchbrackets.js'
  import'codemirror/addon/comment/comment.js'
  import'codemirror/addon/dialog/dialog.js'
  import'codemirror/addon/dialog/dialog.css'
  import'codemirror/addon/search/searchcursor.js'
  import'codemirror/addon/search/search.js'
  import'codemirror/keymap/sublime.js'


  // require more codemirror resource...

  // component
  export default {
    data () {
      return {
        code: 'import requests',
        cmOptions: {
          // codemirror options
          tabSize: 4,
          mode: 'text/x-python',
          theme: 'base16-light',
          lineNumbers: true,
          styleActiveLine: true,
          autoCloseBrackets: true,
          line: true,
          keyMap: "sublime",
          // more codemirror options, 更多 codemirror 的高级配置...
        },
        task: this.code,
        response: "this is a response"

      }
    },
    methods: {
      onCmReady(cm) {
        console.log('the editor is readied!', cm)
      },
      onCmFocus(cm) {
        console.log('the editor is focus!', cm)
      },
      onCmCodeChange(newCode) {
        console.log('this is new code', newCode)
        this.code = newCode
      },
      submit_code() {
        axios.get('/pass')
          .then(function (response) {
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
          });
        console.log(this.code)
      }
    },
    computed: {
      codemirror() {
        return this.$refs.myCm.codemirror
      }
    },
    created() {
      console.log('this is create codemirror object', this.$refs.myCm)
    },
    components: {
      codemirror
    }
  }
</script>

<style>
  html,body,.app {
    height: 100%
  }

  .app {
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
  }

  .code_edit  {
    height: 100%;
    width:50%;
  }

  .vue-codemirror,.CodeMirror{
    height: 100%;

  }


  .task_show {
    height: 50%;
    width:50%;
  }

  .response_show {
    height: 50%;
    width:50%;
  }

</style>
