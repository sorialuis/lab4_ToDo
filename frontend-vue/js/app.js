const app = new Vue({
    el: '#app',
    data: {
        title: 'Lista de tareas',
        newTodo:'',
        todos: [],
        info: null,
    },
    
    methods:{
        refresh(response){
            this.todos = []
            response.data.forEach(element => {
                this.todos.push({
                    id: element[0],
                    title: element[1],
                    done: (element[2] != "Not Started")
                })
            })
        },
        addTodo(){
            // console.log(this.newTodo);
            // Enviar a la api la nueva Todo
            axios
                .post('http://localhost:5001/api/V1/todos', {
                    task : this.newTodo
                })
                .then(response => {
                    this.refresh(response)
                })

            // this.todos.push({
            //     title: this.newTodo,
            //     done: false
            // });
            this.newTodo = '';
            // Refresh las todo
        },
        removeTodo(todo){
            // const todoIndex = this.todos.indexOf(todo);
            // this.todos.splice(todoIndex, 1);
            axios
                .delete('http://localhost:5001/api/V1/todos/' + todo.id)
                .then(response => {
                    this.refresh(response)
                })
            
        },
        updateTodo(todo){
            if(todo.done){
                texto = 'Not Started'
            }else{
                texto =  'Completed'
            }
            axios
       
                .put('http://localhost:5001/api/V1/todos/' + todo.id, {
                    status : texto
                })
                .then(response => {
                    this.refresh(response)
                })
        },
        refreshTodo(){
            axios
                .get('http://localhost:5001/api/V1/todos')
                // .then(response => (
                //     this.info = response.data            
                //     ))

                // .then(response => (
                //     response.data.forEach(element => {
                //         this.todos.push({
                //             id: element[0],
                //             title: element[1],
                //             done: (element[2] != "Not Started")
                //         })
                //     })
                //     ))

                .then(response => { 
                    this.refresh(response)
                })
        }
        
    },
    
    beforeMount(){
        this.refreshTodo()
    },
});

