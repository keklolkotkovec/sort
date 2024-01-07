if (!window["App"]) throw new Error("Critical Error in Application");
(function m(App) {


    //===========================================================================================================


    function lib() {
        var _windowContainer = null,
        _guid = null,
        _poll = this,
        _name = '',
        _store = null;

        var header, panel;

        var save = function(){ //Функция сохранения изменений в анкете
            if (!panel.container['form'].pharmId) return false;

            var modifyData = '';

            $.each(_store.getModifiedRecords(), function(index, rec){
                $.each(rec.modified, function(name){
                    modifyData += '&values['+index+']['+name+']=' + rec.data[name];
                });
                modifyData += '&id['+index+']=' + rec.id;
            });
            if (modifyData == '') return;
                $.getJSON('./modules/units/units.php?action=SET_FORMDATA&pharmId='+panel.container['form'].pharmId+'&projectId='+_param.projectId+'&stageId='+_param.stageId + modifyData +'&rnd='+Math.random(), function(data){
                if (!data || !data.result){
                    alert('ошибка сохранения, попробуйте еще раз');
                    //_store.rejectChanges();
                }else if (data.result == true){
                    _store.commitChanges();
                    panel.container['form'].loadData(panel.container['form'].pharmId);
                }
                $.unblockUI();
            }.bind(this));
        }

        var Header = function (container) {
            var id = 'li[rel = "' + _guid + '"] '+ ".context";
            var template = '<div class="header" style="clear:both; font-size: small;"><div class="context" style="clear:both; overflow:hidden"></div><div class="header_button collapse"></div><div class="buttons">&nbsp;</div></div>';
            Header.superClass.apply(this, [id, template, container]);

            this.appendTo = function (parent) {
                $(parent).append(this.template);
                return this;
            }

            var _expanded = true;

            this.expand = function(callback){
                _expanded = true;
                _windowContainer.find('.header_button').removeClass('expand').addClass('collapse');
                this.element().animate({
                    height: this.container['title'].element().outerHeight() + this.container['description'].element().outerHeight()
                }, "fast", callback);
            }

            this.height = function (height) {
                return _windowContainer.find('.header').outerHeight()
            }

            this.expanded = function(){
                return _expanded;
            }

            this.addButton = function(caption, delegate){
                _windowContainer.find('.buttons').append('<input type="button" id="'+caption+'" value="'+caption+'" />');
                _windowContainer.find('.buttons #'+caption).click(delegate);
            }
