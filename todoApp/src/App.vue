<script setup>
  import { ref } from 'vue'

  const todos = ref([])
  const newTodo = ref('')

  const addTodo = () => {
     todos.value.push({
        title: newTodo.value,
        completed: false,
        id: todos.value.length
     })
     newTodo = ''
  }
  
</script>

<template>
  <form @submit.prevent="addTodo">
    <input type="text" placeholder="add a todo" 
           v-model="newTodo"/>
    <button type="submit">add</button>
  </form>

  <div v-if="todos.length === 0" class="empty-message"> you haven't a todo</div>
  <div v-else class="todos">
     <ul>
       <li v-for="todo in todos" :key="id" v-show="todo.completed == false"> 
        <input type="checkbox" />
        {{ todo.title }}
        <button @click="todo.completed = true ">delete</button>
       </li>
     </ul>

  </div>

</template>

<style scoped>

</style>
