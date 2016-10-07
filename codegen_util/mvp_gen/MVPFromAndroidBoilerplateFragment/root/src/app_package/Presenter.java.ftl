package ${packageName};

import com.shundaojia.travel.ui.base.BasePresenter;

import javax.inject.Inject;

import io.reactivex.disposables.CompositeDisposable;

public class ${className}Presenter extends BasePresenter<${className}MvpView> {

    private CompositeDisposable mCompositeDisposable = new CompositeDisposable();

    @Inject
    public ${className}Presenter() {
    }

    @Override
    public void attachView(${className}MvpView mvpView) {
        super.attachView(mvpView);
    }

    @Override
    public void detachView() {
        super.detachView();
        mCompositeDisposable.clear();
    }
}