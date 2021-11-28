<template>
    <div>
        <!-- select task type to edit -->
        <select v-model="selectedType">
          <option :value="{name: '', attributes: []}" selected>New Task Type</option>
          <option v-for="type in taskTypesCopy" :key="type.name" :value="type">{{ type.name }}
          </option>
        </select>
        <!-- success/error message -->
        <div>{{ message }}</div>
        <input v-if="selectedType.name === ''" v-model="selectedTypeCopy.name" placeholder = "New Task Type Name">
        <table>
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
                <th v-if="addNewAttribute"><input v-model="newAttribute.name" placeholder="New Attribute Name"></th>
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
                <!-- Opens up add new attribute column -->
                <button @click="addNewAttribute = !addNewAttribute">
                    <span v-if="!addNewAttribute">Add New Attribute</span>
                    <span v-else>Cancel</span>
                </button>
                <!-- Saves new attribute -->
                <button v-if="addNewAttribute && newAttribute.name.length > 0 && newAttribute.type.length" @click="saveNewAttribute">Save New Attribute</button>
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
            </tr>
        </table>
        <button v-if="haveMadeChanges" @click="saveTypeChanges">Save Task Type</button>
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
        this.selectedType = { name: '', attributes: [] }
        this.message = ''
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
      this.message = ''
    }
  },
  beforeMount () {
    this.taskTypesCopy = this.taskTypes
  }
}
</script>
