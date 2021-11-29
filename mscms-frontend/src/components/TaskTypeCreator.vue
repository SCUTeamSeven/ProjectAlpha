<template>
    <div class = 'tasktypecreator'>
        <h2>Create/Edit Task Types</h2>
        <!-- select task type to edit -->
        <select v-model="selectedType">
          <option :value="{name: '', attributes: []}" selected>New Task Type</option>
          <option v-for="type in taskTypesCopy" :key="type.name" :value="type">{{ type.name }}
          </option>
        </select>
        <!-- success/error message -->
        <div class = 'message' v-if="message !== ''">{{ message }}</div>
        <input class="newTaskName" v-if="selectedType.name === ''" v-model="selectedTypeCopy.name" placeholder = "New Task Type Name">
        <div class="taskTableOuter">
        <table class='taskTypeTable'>
            <tr>
                <!-- loads global attribute headers -->
                <th v-for="att in globalAttributes" :key="att"> {{ att }} </th>
                <!-- loads task-specific attribute headers -->
                <th v-for="att in selectedTypeCopy.attributes" :key="att.id">
                    <!-- If editing an attribute name, replace the text with an input -->
                    <input v-if="att.id === editingAttribute" v-model="editedAttributeName" placeholder = "Attribute Name">
                    <span v-else>{{ att.name }}</span>
                </th>
                <!-- If adding a new attribute, show an input -->
                <th class="newAttributeName" v-if="addNewAttribute"><input v-model="newAttribute.name" placeholder="New Attribute Name"></th>
            </tr>
            <tr>
                <!-- adds empty cells to account for globals with no att type -->
                <td v-for="att in globalAttributes" :key="att"></td>
                <!-- Load att type for task-specific attributes -->
                <td v-for="att in selectedTypeCopy.attributes" :key="att.id">
                    {{ att.type }}
                </td>
                <!-- If adding a new attribute, add cell with dropdown to select new attribute's type -->
                <td v-if="addNewAttribute">
                    <select v-model="newAttribute.type">
                        <option disabled value="">New Attribute Type</option>
                        <option v-for="type in attributeTypes" :key="type" :value="type">{{ type }}</option>
                    </select>
                </td>
            </tr>
            <tr>
                <!-- adds empty cells to account for globals -->
                <td v-for="att in globalAttributes" :key="att"></td>
                <!-- adds edit/delete function for each att -->
                <td v-for="att in selectedTypeCopy.attributes" :key="att">
                    <button v-if="!(editingAttribute === att.id)" @click="editingAttribute = att.id, editedAttributeName = att.name">edit name</button>
                    <button v-else @click="editingAttribute = ''">cancel</button>
                    <button v-if="(editingAttribute === att.id)" @click="saveEditedAttribute">save</button>
                    <button v-else @click="deleteAttribute(att)">delete</button>
                </td>
                <td v-if="addNewAttribute"></td>
            </tr>
        </table>
        </div>
        <div class='buttonContainer'>
        <!-- Opens up add new attribute column -->
        <button @click="addNewAttribute = !addNewAttribute, newAttribute = { name: '', id: 0, type: '' }">
          <span v-if="!addNewAttribute">Add New Attribute</span>
          <span v-else>Cancel</span>
        </button>
        <!-- Saves new attribute -->
        <button v-if="addNewAttribute && newAttribute.name.length > 0 && newAttribute.type.length" @click="saveNewAttribute">Save New Attribute</button>
        <button style="margin-left:40px;" v-if="haveMadeChanges" @click="saveTypeChanges">Save Task Type</button>
        </div>
    </div>
</template>

<script>
export default {
  props: {
    // gets all existing task types
    taskTypes: Object
  },
  data () {
    return {
      message: '',
      taskTypesCopy: {},
      attributeTypes: ['Short Answer', 'Long Answer', 'Checkbox', 'Date'],
      globalAttributes: ['Building', 'Room', 'Date Assigned', 'Operator'],
      selectedType: { name: '', attributes: [] },
      selectedTypeCopy: { name: '', attributes: [] },
      haveMadeChanges: false,
      addNewAttribute: false,
      newAttribute: { name: '', id: 0, type: '' },
      editingAttribute: '',
      editedAttributeName: ''
    }
  },
  methods: {
    validateNewName: function (name) {
      var validated = 1
      if (name === '') {
        this.message = 'Attribute name cannot be empty.'
        validated = 0
      }
      for (var i in this.specificAttributes) {
        if (name === this.specificAttributes[i].name && name !== this.editingAttribute) {
          validated = 0
          this.message = 'That attribute name already exists.'
        }
      }
      if (validated) {
        this.message = ''
      }
      return validated
    },
    saveNewAttribute: function () {
      if (this.validateNewName(this.newAttribute.name)) {
        this.selectedTypeCopy.attributes.push(this.newAttribute)
        this.addNewAttribute = false
        this.newAttribute = {
          name: '',
          id: this.newAttribute.id++,
          type: ''
        }
        this.haveMadeChanges = true
      }
    },
    saveEditedAttribute: function () {
      if (this.validateNewName(this.editedAttributeName)) {
        this.selectedTypeCopy.attributes[this.editingAttribute].name = this.editedAttributeName
        this.editingAttribute = ''
        this.haveMadeChanges = true
      }
    },
    deleteAttribute: function (attribute) {
      if (confirm("Deleting will erase this attribute's data for all instances of this task. Are you sure you want to delete?")) {
        var x = this.selectedTypeCopy.attributes
        this.selectedTypeCopy.attributes = []
        for (var i in x) {
          if (attribute !== x[i]) {
            this.selectedTypeCopy.attributes.push(x[i])
          }
        }
        this.haveMadeChanges = true
      }
    },
    saveTypeChanges: function () {
      // Delete SelectedType from task type list (only if not adding a brand new attribute)
      if (this.selectedType.name !== '') {
        var x = this.taskTypesCopy
        this.taskTypesCopy = []
        for (var i in x) {
          if (this.selectedType !== x[i]) {
            this.taskTypesCopy.push(x[i])
          }
        }
      }
      // If selected type copy name is not empty, add it to the task type list
      // Make api call to send updated task to database
      if (this.selectedTypeCopy.name === '') {
        this.message = 'New task type name cannot be empty.'
      } else {
        this.taskTypesCopy.push(this.selectedTypeCopy)
        this.message = 'Task Type successfully saved.'
        this.haveMadeChanges = false
        this.addNewAttribute = false
        var message = this.selectedTypeCopy.name + ' successfully saved!'
        this.selectedType = { name: '', attributes: [] }
        this.message = message
        this.$emit('updateTaskTypes', this.taskTypesCopy)
      }
    }
  },
  watch: {
    selectedType: function () {
      // Create a copy of the selected type, and edit the copy. This is necessary for a safe function to be implemented without complications
      this.selectedTypeCopy = JSON.parse(JSON.stringify(this.selectedType))
      this.newAttribute.id = this.selectedType.attributes.length - 1
      this.addNewAttribute = false
    }
  },
  beforeMount () {
    this.taskTypesCopy = this.taskTypes
  }
}
</script>

<style>
.tasktypecreator{
  width: calc(100% - 160px);
  margin: 40px;
  padding: 40px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  border-radius: 20px;
  border:1px solid gray;
  background-color: rgb(246, 246, 246);
}
.tasktypecreator h2 {
  margin: 0 0 30px;
  font-size:30px;
}
.tasktypecreator select{
  border: 1px solid #cbcbcb;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}
.tasktypecreator button {
  padding: 15px 20px;
  border: 1px solid #cbcbcb;
  color: #7c7c7c;
  background-color: white;
  border-radius: 5px;
  font-size: 14px;
  transition:.2s;
  cursor: pointer;
}
.taskTypeTable button {
    padding: 5px;
}
.tasktypecreator button:hover {
  color:black;
  border: 1px solid black;
}
.buttonContainer {
  display:flex;
  padding-top:30px;
}
.newTaskName {
  padding: 9px;
  border: 1px solid black;
  background-color: white;
  border-radius: 5px;
  font-size: 16px;
  margin-top:30px;
}
.newTaskName::placeholder {
  color:rgb(85, 85, 85);
}

 .taskTableOuter {
   overflow: hidden;
   border-radius: 20px;
   border:1px solid gray;
   margin-top:30px;
 }
 .taskTypeTable{
   width:100%;
   border-collapse: collapse;
 }

.newAttributeName {
  padding:0;
}
.newAttributeName input {
  height: 25px;
  width: 90%;
  background-color: transparent;
  border: solid black;
  border-width: 0 0 1px 0;
  font-size:16px;
}
.message {
  margin-top: 30px;
border: 1px solid black;
padding: 20px;
width: 50%;
border-radius: 5px;
background-color: rgb(217, 217, 217);
}
.newAttributeName input::placeholder {
  color:black;
}
/* styles for headers and cells */
.taskTypeTable th {
  background-color:#b8bbbd;
  border:solid gray;
  border-width: 0 1px 1px 1px;
  padding:10px 15px;
}
.taskTypeTable td {
  text-align:center;
  border: 1px solid #c4c8cb;
  font-size:14px;
  padding:10px;
  background-color: white
}
.taskTypeTable tr{
  height:48px;
}
/* hide border for edge cells */
.taskTypeTable th:first-child, .taskTypeTable td:first-child{
  border-left:none;
}
.taskTypeTable th:last-child, .taskTypeTable td:last-child{
  border-right:none;
}
.taskTypeTable tr:last-child td{
  border-bottom:none;
}
</style>
