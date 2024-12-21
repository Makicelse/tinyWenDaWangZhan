<template>
  <div :class="[ 'message', roleType ]">
    {{ message.role }}: {{ message.content }}
  </div>
</template>

<script>
export default {
    name: 'messageBubble',
    props: ['message'], 
    computed: {
      roleType () {
        return this.message.role === 'user' ? 'user' : 'assistant';
      }
    }
}
</script>

<style>
.message {
    border: 1px solid #ccc;
    border-radius: 7px;
    padding: 7px 13px;
    margin: 7px;
    max-width: 700px;
}

.user {
    background-color: #90EE90;
}

.assistant {
    background-color: #fff;
    /* margin-bottom: 18px; */
}
</style>