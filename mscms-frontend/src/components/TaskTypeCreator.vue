<template>
    <div>
        <select v-model="selectedTemplate">
          <option :value="{name: '', attributes: []}" selected>New Task Template</option>
          <option v-for="template in taskTemplates" :key="template" :value="template">{{ template.name }}
          </option>
        </select>
        <div>{{ message }}</div>
        <table>
            <tr>
                <th v-for="attribute in globalAttributes" :key="attribute"> {{ attribute.name }} </th>
                <th v-for="attribute in specificAttributes" :key="attribute">
                    <input v-if="attribute.name === editingAttribute" v-model="editedAttributeName" placeholder = "Attribute Name">
                    <span v-else>{{ attribute.name }}</span>
                </th>
                <th v-if="addNewAttribute"><input v-model="newAttributeName" placeholder="New Attribute Name"></th>
            </tr>
            <tr>
                <td v-for="attribute in globalAttributes" :key="attribute"> {{ attribute.type }} </td>
                <td v-for="attribute in specificAttributes" :key="attribute">
                    {{ attribute.type }}
                </td>
                <td v-if="addNewAttribute">
                    <select v-model="newAttributeType">
                        <option disabled value="">New Attribute Type</option>
                        <option v-for="type in possibleTaskTypes" :key="type" :value="type">{{ type }}</option>
                    </select>
                </td>
                <button @click="addNewAttribute = !addNewAttribute">
                    <span v-if="!addNewAttribute">Add New Attribute</span>
                    <span v-else>Cancel</span>
                </button>
                <button v-if="addNewAttribute && newAttributeName.length > 0 && newAttributeType.length" @click="saveNewAttribute">Save New Attribute</button>
            </tr>
            <tr>
                <td v-for="attribute in globalAttributes" :key="attribute"></td>
                <td v-for="attribute in specificAttributes" :key="attribute">
                    <button v-if="!(editingAttribute === attribute.name)" @click="editingAttribute = attribute.name, editedAttributeName = attribute.name">edit name</button>
                    <button v-else @click="editingAttribute = ''">cancel</button>
                    <button v-if="(editingAttribute === attribute.name)" @click="saveEditedAttribute">save</button>
                    <button v-else @click="deleteAttribute(attribute)">delete</button>
                </td>
            </tr>
        </table>
        <button v-if="haveMadeChanges" @click="saveTemplateChanges">Save Task Template</button>
    </div>
</template>

<script>
var globals = [
  {
    name: 'Building',
    type: ''
  },
  {
    name: 'Room',
    type: ''
  },
  {
    name: 'Date Assigned',
    type: 'Date'
  },
  {
    name: 'Operator',
    type: ''
  }
]
var specifics = [
  {
    name: 'Task Attribute 1',
    type: 'Small Text Field'
  },
  {
    name: 'Task Attribute 2',
    type: 'Checkbox'
  },
  {
    name: 'Task Attribute 3',
    type: 'Dropdown'
  },
  {
    name: 'Task Attribute 4',
    type: 'Large Text Field'
  }
]
var types = [
  'Short Answer',
  'Long Answer',
  'Checkbox',
  'Dropdown',
  'Date'
]
var templates = [
  {
    name: 'Task Template 1',
    attributes: specifics
  },
  {
    name: 'Task Template 2',
    attributes: specifics
  },
  {
    name: 'Task Template 3',
    attributes: specifics
  },
  {
    name: 'Task Template 4',
    attributes: specifics
  }
]
export default {
  data () {
    return {
      message: '',
      selectedTemplate: { name: '', attributes: [] },
      taskTemplates: [],
      haveMadeChanges: false,
      globalAttributes: [],
      specificAttributes: [],
      possibleTaskTypes: [],
      addNewAttribute: false,
      newAttributeName: '',
      newAttributeType: '',
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
      if (this.validateNewName(this.newAttributeName)) {
        var name = this.newAttributeName
        var type = this.newAttributeType
        this.specificAttributes.push({ name, type })
        this.addNewAttribute = false
        this.newAttributeName = ''
        this.newAttributeType = ''
        this.haveMadeChanges = true
      }
    },
    saveEditedAttribute: function () {
      if (this.validateNewName(this.editedAttributeName)) {
        for (var i in this.specificAttributes) {
          if (this.specificAttributes[i].name === this.editingAttribute) {
            this.specificAttributes[i].name = this.editedAttributeName
            this.editingAttribute = ''
            this.haveMadeChanges = true
          }
        }
      }
    },
    deleteAttribute: function (attribute) {
      if (confirm("Deleting will erase this attribute's data for all instances of this task. Are you sure you want to delete?")) {
        this.specificAttributes.splice(attribute, 1)
        this.haveMadeChanges = true
      }
    },
    saveTemplateChanges: function () {
      // make api call here
      console.log(this.taskType, this.specificAttributes)
      this.message = 'Task Template successfully saved.'
      this.haveMadeChanges = false
    },
    getTaskTemplates: function () {
      // api call here
      for (var i in templates) {
        this.taskTemplates.push(templates[i])
      }
    },
    getGlobalAttributes: function () {
      // make api call here
      this.globalAttributes = globals
    },
    getSpecificAttributes: function (template) {
      this.specificAttributes = template.attributes
    },
    getPossibleTaskTypes: function () {
      // make api call here
      this.possibleTaskTypes = types
    }

  },
  watch: {
    selectedTemplate: function () {
      this.getSpecificAttributes(this.selectedTemplate)
    }
  },
  beforeMount () {
    this.getTaskTemplates()
    this.getPossibleTaskTypes()
    this.getGlobalAttributes()
    this.getSpecificAttributes(this.selectedTemplate)
  }
}
</script>
