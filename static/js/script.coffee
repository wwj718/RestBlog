class BlogView extends Backbone.View
  events:
    #"click .delete": "removeItem"
    "click .text": "modifyItem"
  initialize: ->
    @model.bind 'change', @render
    @model.bind 'destroy', @unrender
  removeItem: =>
    @model.destroy()
  modifyItem: =>
    new_value = window.prompt "title","input title"
    @model.set 'title', new_value
    new_value = window.prompt "content","input content"
    @model.set 'content', new_value
    @model.save()
  render: =>
    $(@el).html "<p><span class='text'>#{@model.get 'title'}:#{@model.get 'content'}</span><span class='delete'>x</span></p>"
    @
  unrender: =>
    @el.remove()

class BlogModel extends Backbone.Model
  #default
  render: =>
    myview = new BlogView model: @  #@ is self,so it is BlogModel
    $(".contents").append  myview.render().el #el is new div? yes

class BlogList extends Backbone.Collection
  model: BlogModel
  url: "/api/blog/" #item'url will be /blog/:id auto
  initialize: =>
    @bind 'add', (item) ->
      #alert 'haha'
      item.render() #item , it is BlogModel
    @bind 'reset', (item) ->
      Blog.render() for Blog in item.models # render in view
    @fetch()  #will get what json object list?
$ ->
  window.bloglist = new BlogList()
  $("button").click ->
    window.bloglist.create new BlogModel title: $("input").val() #title